from config import settings
from common.query import Query


class SpyseAPI(Query):
    def __init__(self, domain):
        Query.__init__(self)
        self.domain = domain
        self.module = 'Dataset'
        self.source = 'SpyseAPIQuery'
        self.token = settings.spyse_api_token

    def query(self):
        """
        Query the subdomain from the interface and do subdomain matching
                """
        limit = 100
        offset = 0
        while True:
            self.header = self.get_header()
            self.header.update({'Authorization': 'Bearer ' + self.token})
            self.proxy = self.get_proxy(self.source)
            addr = 'https://api.spyse.com/v3/data/domain/subdomain'
            params = {'domain': self.domain, 'offset': offset, 'limit': limit}
            resp = self.get(addr, params)
            if not resp:
                return
            json = resp.json()
            subdomains = self.match_subdomains(str(json))
            if not subdomains:  # Stop querying if no subdomains are found
                break
            self.subdomains.update(subdomains)
            offset += limit
            if len(json.get('data').get('items')) < limit:
                break

    def run(self):
        """
        Class execution entry
        """
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
        query = SpyseAPI(domain)
        query.run()

    if __name__ == '__main__':
        run('example.com')