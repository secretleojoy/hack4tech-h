"""
Check the crossdomain.xml file to collect subdomains
"""
from common.check import Check


class CrossDomain(Check):
    def __init__(self, domain):
        Check.__init__(self)
        self.domain = domain
        self.module = 'check'
        self.source = "CrossDomainCheck"

    def check(self):
        """
        Check crossdomain.xml to collect subdomains
        """
        filenames = {'crossdomain.xml'}
        self.to_check(filenames)

    def run(self):
        """
        Class execution entry
        """
        self.begin()
        self.check()
        self.finish()
        self.save_json()
        self.gen_result()
        self.save_db()


def run(domain):
    """
    Class uniform call entry

    :param domain: domain name
    """
    check = CrossDomain(domain)
    check.run()


if __name__ == '__main__':
    run('example.com')
