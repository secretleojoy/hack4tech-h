import time
from config import settings
from common.search import Search


class BingAPI(Search):
    def __init__(self, domain):
        Search.__init__(self)
        self.domain = domain
        self.module ='Search'
        self.source ='BingAPISearch'
        self.addr ='https://api.cognitive.microsoft.com/bing/v7.0/search'
        self.id = settings.bing_api_id
        self.key = settings.bing_api_key
        self.limit_num = 1000 # Bing limits the number of searches for the same search keyword
        self.delay = 1 # Bing custom search limit delay is 1 second

    def search(self, domain, filtered_subdomain=''):
        """
        Send search request and do subdomain matching

        :param str domain: domain name
        :param str filtered_subdomain: filtered subdomain
        """
        self.page_num = 0 # Reset the second search to 0
        while True:
            time.sleep(self.delay)
            self.header = self.get_header()
            self.header = {'Ocp-Apim-Subscription-Key': self.key}
            self.proxy = self.get_proxy(self.source)
            query ='site:.' + domain + filtered_subdomain
            params = {'q': query,'safesearch':'Off',
                      'count': self.per_page_num,
                      'offset': self.page_num}
            resp = self.get(self.addr, params)
            subdomains = self.match_subdomains(resp)
            if not self.check_subdomains(subdomains):
                break
            self.subdomains.update(subdomains)
            self.page_num += self.per_page_num
            if self.page_num >= self.limit_num: # search limit
                break

    def run(self):
        """
        Class execution entry
        """
        if not self.have_api(self.id, self.key):
            return
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
    search = BingAPI(domain)
    search.run()


if __name__ =='__main__':
    run('example.com')