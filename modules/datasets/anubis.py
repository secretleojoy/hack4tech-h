from common.query import Query


class Anubis(Query):
    def __init__(self, domain):
        Query.__init__(self)
        self.domain = domain
        self.module = 'Dataset'
        self.source = 'AnubisQuery'
        self.addr = 'https://jldc.me/anubis/subdomains/'

    def query(self):
        """
        Query the subdomain from the interface and do subdomain matching
        """
        self.header = self.get_header()
        self.proxy = self.get_proxy(self.source)
        self.addr = self.addr + self.domain
        resp = self.get(self.addr)
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
    query = Anubis(domain)
    query.run()


if __name__ == '__main__':
    run('hackerone.com')
