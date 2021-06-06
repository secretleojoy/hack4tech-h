from common.query import Query


class ThreatMiner(Query):
    def __init__(self, domain):
        Query.__init__(self)
        self.domain = domain
        self.module = 'Intelligence'
        self.source = 'ThreatMinerQuery'
        self.addr = 'https://www.threatminer.org/getData.php'

    def query(self):
        """
        Query the subdomain from the interface and do subdomain matching
                 """
        self.header = self.get_header()
        self.proxy = self.get_proxy(self.source)
        params = {'e': 'subdomains_container',
                  'q': self.domain, 't': 0, 'rt': 10}
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
        query = ThreatMiner(domain)
        query.run()

    if __name__ == '__main__':
        run('example.com')