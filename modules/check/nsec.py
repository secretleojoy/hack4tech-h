# https://www.icann.org/resources/pages/dnssec-what-is-it-why-important-2019-03-20-zh
# https://appsecco.com/books/subdomain-enumeration/active_techniques/zone_walking.html

from common import utils
from common.check import Check


class NSEC(Check):
    def __init__(self, domain):
        Check.__init__(self)
        self.domain = domain
        self.module = 'check'
        self.source = "NSECCheck"

    def walk(self):
        domain = self.domain
        while True:
            answer = utils.dns_query(domain, 'NSEC')
            if answer is None:
                break
            subdomain = str()
            for item in answer:
                record = item.to_text()
                subdomains = self.match_subdomains(record)
                subdomain = ''.join(subdomains)  # In fact, the length of subdomains here is 1, which means there will only be one subdomain
                self.subdomains.update(subdomains)
            if subdomain == self.domain:  # When the subdomain is found to be the main domain, it means that a cycle has been completed and the query will not continue
                break
            domain = subdomain
        return self.subdomains

    def run(self):
        """
        Class execution entry
        """
        self.begin()
        self.walk()
        self.finish()
        self.save_json()
        self.gen_result()
        self.save_db()


def run(domain):
    """
    Class uniform call entry

    :param str domain: domain name
    """
    brute = NSEC(domain)
    brute.run()


if __name__ == '__main__':
    run('iana.org')
