import time
from common.search import Search


class Yandex(Search):
    def __init__(self, domain):
        Search.__init__(self)
        self.domain = domain
        self.module ='Search'
        self.source ='YandexSearch'
        self.init ='https://yandex.com/'
        self.addr ='https://yandex.com/search'
        self.limit_num = 1000 # Limit the number of searches
        self.delay = 5

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
        self.cookie = resp.cookies # Get cookies
        while True:
            time.sleep(self.delay)
            self.proxy = self.get_proxy(self.source)
            query ='site:.' + domain + filtered_subdomain
            params = {'text': query,'p': self.page_num,
                      'numdoc': self.per_page_num}
            resp = self.get(self.addr, params)
            subdomains = self.match_subdomains(resp, fuzzy=False)
            if not self.check_subdomains(subdomains):
                break
            self.subdomains.update(subdomains)
            if'>next</a>' not in resp.text: # Stop searching when the next page does not appear on the search page
                break
            self.page_num += 1
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
    search = Yandex(domain)
    search.run()


if __name__ =='__main__':
    run('example.com')