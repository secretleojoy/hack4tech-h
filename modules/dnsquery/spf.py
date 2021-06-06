from common.lookup import Lookup


class QuerySPF(Lookup):
    def __init__(self, domain):
        Lookup.__init__(self)
        self.domain = domain
        self.module = 'dnsquery'
        self.source = "QuerySPF"
        self.qtype = 'SPF'  # The SPF record collection subdomain of the DNS record used

    def run(self):
        """
        Class execution entry
        """
        self.begin()
        self.query()
        self.finish()
        self.save_json()
        self.gen_result()
        self.save_db()


def run(domain):
    """
    Class uniform call entry

    :param str domain: domain name
    """
    brute = QuerySPF(domain)
    brute.run()


if __name__ == '__main__':
    run('qq.com')