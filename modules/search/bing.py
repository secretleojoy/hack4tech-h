import time
from common.search import Search


class Bing(Search):
    def __init__(self, domain):
        Search.__init__(self)
        self.domain = domain
        self.module ='Search'
        self.source ='BingSearch'
        self.init ='https://www.bing.com/'
        self.addr ='https://www.bing.com/search'
        self.limit_num = 1000 # Limit the number of searches

    def search(self, domain, filtered_subdomain=''):
        """
        Send search request and do subdomain matching

        :param str domain: domain name
        :param str filtered_subdomain: filtered subdomain
        """
        self.header = self.get_header()
        self.proxy = self.get_proxy(self.source)
        self.page_num = 0 # Reset the second search to 0
        resp = self.get(self.init)
        if not resp:
            return
        self.cookie = resp.cookies # Get cookie bing needs to bring cookie when searching
        while True:
            time.sleep(self.delay)
            self.proxy = self.get_proxy(self.source)
            query ='site:.' + domain + filtered_subdomain
            params = {'q': query,'first': self.page_num,
                      'count': self.per_page_num}
            resp = self.get(self.addr, params)
            subdomains = self.match_subdomains(resp, fuzzy=False)
            if not self.check_subdomains(subdomains):
                break
            self.subdomains.update(subdomains)
            # Stop searching when the next page does not appear on the search page
            if'<div class="sw_next">' not in resp.text:
                break
            self.page_num += self.per_page_num
            if self.page_num >= self.limit_num: # search limit
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
    search = Bing(domain)
    search.run()


if __name__ =='__main__':
    run('example.com')