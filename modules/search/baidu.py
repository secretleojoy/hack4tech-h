import time
from bs4 import BeautifulSoup
from common.search import Search


class Baidu(Search):
    def __init__(self, domain):
        Search.__init__(self)
        self.module ='Search'
        self.source ='BaiduSearch'
        self.addr ='https://www.baidu.com/s'
        self.domain = domain
        self.limit_num = 750 # Limit the number of searches

    def redirect_match(self, html):
        """
        Get the jump address and pass the address to make a jump head request

        :param html: response body
        :return: subdomain
        """
        bs = BeautifulSoup(html,'html.parser')
        subdomains_all = set()
        # Get all the redirect URL addresses in the search results
        for find_res in bs.find_all('a', {'class':'c-showurl'}):
            url = find_res.get('href')
            subdomains = self.match_location(url)
            subdomains_all.update(subdomains)
        return subdomains_all

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
            self.proxy = self.get_proxy(self.source)
            query ='site:.' + domain + filtered_subdomain
            params = {'wd': query,
                      'pn': self.page_num,
                      'rn': self.per_page_num}
            resp = self.get(self.addr, params)
            if not resp:
                return
            if len(domain)> 12: # Solve the problem of incomplete display of domain names in Baidu search results
                # Get the Location field of the Baidu redirect URL response header to get the direct link
                subdomains = self.redirect_match(resp.text)
            else:
                subdomains = self.match_subdomains(resp, fuzzy=False)
            if not self.check_subdomains(subdomains):
                break
            self.subdomains.update(subdomains)
            self.page_num += self.per_page_num
            # Stop searching when the next page does not appear on the search page
            if f'&pn={self.page_num}&' not in resp.text:
                break
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
    search = Baidu(domain)
    search.run()


if __name__ =='__main__':
    run('mi.com')