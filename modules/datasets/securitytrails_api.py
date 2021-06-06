from config import settings
from common.query import Query


class SecurityTrailsAPI(Query):
    def __init__(self, domain):
        Query.__init__(self)
        self.domain = domain
        self.module ='Dataset'
        self.source ='SecurityTrailsAPIQuery'
        self.addr ='https://api.securitytrails.com/v1/domain/'
        self.api = settings.securitytrails_api
        self.delay = 2 # SecurityTrails query delay is at least 2 seconds

    def query(self):
        """
        Query the subdomain from the interface and do subdomain matching
        """
        self.header = self.get_header()
        self.proxy = self.get_proxy(self.source)
        params = {'apikey': self.api}
        url = f'{self.addr}{self.domain}/subdomains'
        resp = self.get(url, params)
        if not resp:
            return
        prefixs = resp.json()['subdomains']
        subdomains = [f'{prefix}.{self.domain}' for prefix in prefixs]
        if subdomains:
            self.subdomains.update(subdomains)

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
    query = SecurityTrailsAPI(domain)
    query.run()


if __name__ =='__main__':
    run('example.com')