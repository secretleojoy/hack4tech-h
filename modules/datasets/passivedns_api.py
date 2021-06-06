from config import settings
from common.query import Query


class PassiveDnsAPI(Query):
    def __init__(self, domain):
        Query.__init__(self)
        self.domain = domain
        self.module = 'Dataset'
        self.source = 'PassiveDnsQuery'
        self.addr = settings.passivedns_api_addr or 'http://api.passivedns.cn'
        self.token = settings.passivedns_api_token

    def query(self):
        """
        Query the subdomain from the interface and do subdomain matching
                 """
        self.header = self.get_header()
        self.header.update({'X-AuthToken': self.token})
        self.proxy = self.get_proxy(self.source)
        url = self.addr + '/flint/rrset/*.' + self.domain
        resp = self.get(url)
        self.subdomains = self.collect_subdomains(resp)

    def run(self):
        """
        Class execution entry
        """
        if 'api.passivedns.cn' in self.addr:
            if not self.have_api(self.token):
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
        query = PassiveDnsAPI(domain)
        query.run()

    if __name__ == '__main__':
        run('example.com')