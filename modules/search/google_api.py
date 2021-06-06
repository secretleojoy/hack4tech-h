import time
from config import settings
from common.search import Search


class GoogleAPI(Search):
    def __init__(self, domain):
        Search.__init__(self)
        self.domain = domain
        self.module ='Search'
        self.source ='GoogleAPISearch'
        self.addr ='https://www.googleapis.com/customsearch/v1'
        self.delay = 1
        self.key = settings.google_api_key
        self.id = settings.google_api_id
        self.per_page_num = 10 # Only 10 results can be requested at a time

    def search(self, domain, filtered_subdomain=''):
        """
        Send search request and do subdomain matching

        :param str domain: domain name
        :param str filtered_subdomain: filtered subdomain
        """
        self.page_num = 1
        while True:
            word ='site:.' + domain + filtered_subdomain
            time.sleep(self.delay)
            self.header = self.get_header()
            self.proxy = self.get_proxy(self.source)
            params = {'key': self.key,'cx': self.id,
                      'q': word,'fields':'items/link',
                      'start': self.page_num,'num': self.per_page_num}
            resp = self.get(self.addr, params)
            subdomains = self.match_subdomains(resp)
            if not self.check_subdomains(subdomains):
                break
            self.subdomains.update(subdomains)
            self.page_num += self.per_page_num
            if self.page_num> 100: # Free API can only query the first 100 results
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
    search = GoogleAPI(domain)
    search.run()


if __name__ =='__main__':
    run('mi.com')