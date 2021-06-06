
from common.query import Query


class SiteDossier(Query):
    def __init__(self, domain):
        Query.__init__(self)
        self.domain = domain
        self.module = 'Dataset'
        self.source = 'SiteDossierQuery'
        self.addr = 'http://www.sitedossier.com/parentdomain/'
        self.delay = 2
        self.page_num = 1
        self.per_page_num = 100

    def query(self):
        """
        Query the subdomain from the interface and do subdomain matching
                """
        while True:
            self.header = self.get_header()
            self.proxy = self.get_proxy(self.source)
            url = f'{self.addr}{self.domain}/{self.page_num}'
            resp = self.get(url)
            subdomains = self.match_subdomains(resp)
            if not subdomains:  # Stop querying if no subdomains are found
                break
            self.subdomains.update(subdomains)
            # Stop searching when the next page does not appear on the search page
            if 'Show next 100 items' not in resp.text:
                break
            self.page_num += self.per_page_num

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
        query = SiteDossier(domain)
        query.run()

    if __name__ == '__main__':
        run('example.com')