from config import settings
from common.query import Query


class VirusTotalAPI(Query):
    def __init__(self, domain):
        Query.__init__(self)
        self.domain = domain
        self.module = 'Intelligence'
        self.source = 'VirusTotalAPIQuery'
        self.key = settings.virustotal_api_key

    def query(self):
        """
        Query the subdomain from the interface and do subdomain matching
                """
        next_cursor = ''
        while True:
            self.header = self.get_header()
            self.header.update({'x-apikey': self.key})
            self.proxy = self.get_proxy(self.source)
            params = {'limit': '40', 'cursor': next_cursor}
            addr = f'https://www.virustotal.com/api/v3/domains/{self.domain}/subdomains'
            resp = self.get(url=addr, params=params)
            subdomains = self.match_subdomains(resp)
            if not subdomains:
                break
            self.subdomains.update(subdomains)
            data = resp.json()
            next_cursor = data.get('meta').get('cursor')

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
        query = VirusTotalAPI(domain)
        query.run()

    if __name__ == '__main__':
        run('mi.com')