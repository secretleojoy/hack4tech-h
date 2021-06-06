from common.lookup import Lookup


class QueryTXT(Lookup):
    def __init__(self, domain):
        Lookup.__init__(self)
        self.domain = domain
        self.module = 'dnsquery'
        self.source = "QueryTXT"
        self.qtype = 'TXT'  # The TXT record collection subdomain of the used DNS record

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
    query = QueryTXT(domain)
    query.run()


if __name__ == '__main__':
    run('cuit.edu.cn')