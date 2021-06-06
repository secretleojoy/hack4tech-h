from common.search import Search


class Sogou(Search):
    def __init__(self, domain):
        Search.__init__(self)
        self.domain = domain
        self.module ='Search'
        self.source ='SogouSearch'
        self.addr ='https://www.sogou.com/web'
        self.limit_num = 1000 # Limit the number of searches

    def search(self, domain, filtered_subdomain=''):
        """
        Send search request and do subdomain matching

        :param str domain: domain name
        :param str filtered_subdomain: filtered subdomain
        """
        self.page_num = 1
        while True:
            self.header = self.get_header()
            self.proxy = self.get_proxy(self.source)
            word ='site:.' + domain + filtered_subdomain
            payload = {'query': word,'page': self.page_num,
                       "num": self.per_page_num}
            resp = self.get(self.addr, payload)
            subdomains = self.match_subdomains(resp, fuzzy=False)
            if not self.check_subdomains(subdomains):
                break
            self.subdomains.update(subdomains)
            self.page_num += 1
            # Stop searching when the next page does not appear on the search page
            if'<a id="sogou_next"' not in resp.text:
                break
            # Search limit
            if self.page_num * self.per_page_num >= self.limit_num:
                break

    def run(self):
        """
        Class execution entry
        """
        self.begin()
        self.search(self.domain)

        # Exclude subdomains with too many search results for the same subdomain to discover new subdomains
        for statement in self.filter(self.domain, self.subdomains):
            self.search(self.domain, filtered_subdomain=statement)

        # Recursively search the subdomains of the next layer
        if self.recursive_search:
            for subdomain in self.recursive_subdomain():
                self.search(subdomain)
        self.finish()
        self.save_json()
        self.gen_result()
        self.save_db()


def run(domain):
    """
    Class uniform call entry

    :param str domain: domain name
    """
    search = Sogou(domain)
    search.run()


if __name__ =='__main__':
    run('example.com')