from config import settings
from common.query import Query


class ThreatBookAPI(Query):
    def __init__(self, domain):
        Query.__init__(self)
        self.domain = domain
        self.module = 'Intelligence'
        self.source = 'ThreatBookAPIQuery'
        self.addr = 'https://api.threatbook.cn/v3/domain/sub_domains'
        self.key = settings.threatbook_api_key

    def query(self):
        """
        Query the subdomain from the interface and do subdomain matching
                 """
        self.header = self.get_header()
        self.proxy = self.get_proxy(self.source)
        params = {'apikey': self.key,
                  'resource': self.domain}
        resp = self.post(self.addr, params)
        self.subdomains = self.collect_subdomains(resp)

    def run(self):
        """
        Class execution entry
        """
        if not self.have_api(self.key):
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
        query = ThreatBookAPI(domain)
        query.run()

    if __name__ == '__main__':
        run('example.com')