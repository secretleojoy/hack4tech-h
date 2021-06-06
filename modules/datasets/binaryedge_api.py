from config import settings
from common.query import Query


class BinaryEdgeAPI(Query):
    def __init__(self, domain):
        Query.__init__(self)
        self.domain = domain
        self.module = 'Dataset'
        self.source = 'BinaryEdgeAPIQuery'
        self.addr = 'https://api.binaryedge.io/v2/query/domains/subdomain/'
        self.api = settings.binaryedge_api

    def query(self):
        """
        Query the subdomain from the interface and do subdomain matching
        """
        self.header = self.get_header()
        self.header.update({'X-Key': self.api})
        self.proxy = self.get_proxy(self.source)
        url = self.addr + self.domain
        resp = self.get(url)
        self.subdomains = self.collect_subdomains(resp)

    def run(self):
        """
        Class execution entry
        """
        if not self.have_api(self.api):
            return
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
    query = BinaryEdgeAPI(domain)
    query.run()


if __name__ == '__main__':
    run('example.com')
