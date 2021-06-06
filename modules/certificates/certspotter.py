from common.query import Query


class CertSpotter(Query):
    def __init__(self, domain):
        Query.__init__(self)
        self.domain = domain
        self.module = 'Certificate'
        self.source = 'CertSpotterQuery'
        self.addr = 'https://api.certspotter.com/v1/issuances'

    def query(self):
        """
        Query the subdomain from the interface and do subdomain matching
        """
        self.header = self.get_header()
        self.proxy = self.get_proxy(self.source)
        params = {'domain': self.domain,
                  'include_subdomains': 'true',
                  'expand': 'dns_names'}
        resp = self.get(self.addr, params)
        self.subdomains = self.collect_subdomains(resp)

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
    query = CertSpotter(domain)
    query.run()


if __name__ == '__main__':
    run('example.com')
