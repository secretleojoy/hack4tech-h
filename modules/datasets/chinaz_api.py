from config import settings
from common.query import Query


class ChinazAPI(Query):
    def __init__(self, domain):
        Query.__init__(self)
        self.domain = domain
        self.module = 'Dataset'
        self.source = 'ChinazAPIQuery'
        self.addr = 'https://apidata.chinaz.com/CallAPI/Alexa'
        self.api = settings.chinaz_api

    def query(self):
        """
        Query the subdomain from the interface and do subdomain matching
        """
        self.header = self.get_header()
        self.proxy = self.get_proxy(self.source)
        params = {'key': self.api, 'domainName': self.domain}
        resp = self.get(self.addr, params)
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
    query = ChinazAPI(domain)
    query.run()


if __name__ == '__main__':
    run('example.com')
