import time
from common.search import Search


class Yahoo(Search):
    def __init__(self, domain):
        Search.__init__(self)
        self.domain = domain
        self.module ='Search'
        self.source ='YahooSearch'
        self.init ='https://search.yahoo.com/'
        self.addr ='https://search.yahoo.com/search'
        self.limit_num = 1000 # Yahoo limits the number of searches
        self.delay = 2
        self.per_page_num = 30 # Yahoo maximum number of items per search

    def search(self, domain, filtered_subdomain=''):
        """
        Send search request and do subdomain matching

        :param str domain: domain name
        :param str filtered_subdomain: filtered subdomain
        """
        self.header = self.get_header()
        self.proxy = self.get_proxy(self.source)
        resp = self.get(self.init)
        if not resp:
            return
        self.cookie = resp.cookies # Get cookies Yahoo needs to bring cookies when searching
        while True:
            time.sleep(self.delay)
            self.proxy = self.get_proxy(self.source)
            query ='site:.' + domain + filtered_subdomain
            params = {'p': query,'b': self.page_num,'pz': self.per_page_num}
            resp = self.get(self.addr, params)
            if not resp:
                return
            text = resp.text.replace('<b>','').replace('</b>','')
            subdomains = self.match_subdomains(text, fuzzy=False)
            if not self.check_subdomains(subdomains):
                break
            self.subdomains.update(subdomains)
            if'>Next</a>' not in resp.text: # Stop searching when the next page does not appear on the search page
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
    search = Yahoo(domain)
    search.run()


if __name__ =='__main__':
    run('example.com')