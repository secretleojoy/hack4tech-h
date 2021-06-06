import hashlib
import re
import time
from urllib import parse

from common.query import Query


class NetCraft(Query):
    def __init__(self, domain):
        Query.__init__(self)
        self.domain = domain
        self.module = 'Dataset'
        self.source = 'NetCraftQuery'
        self.init = 'https://searchdns.netcraft.com/'
        self.addr = 'https://searchdns.netcraft.com/?restriction=site+contains'
        self.page_num = 1
        self.per_page_num = 20

    def bypass_verification(self):
        """
        Bypass NetCraft's JS verification
                """
        resp = self.get(self.init)
        if not resp:
            return False
        self.cookie = resp.cookies
        cookie_value = self.cookie['netcraft_js_verification_challenge']
        cookie_encode = parse.unquote(cookie_value).encode('utf-8')
        verify_taken = hashlib.sha1(cookie_encode).hexdigest()
        self.cookie['netcraft_js_verification_response'] = verify_taken
        return True

    def query(self):
        """
        Query the subdomain from the interface and do subdomain matching
        """
        self.header = self.get_header()  # NetCraft will check User-Agent
        self.proxy = self.get_proxy(self.source)
        if not self.bypass_verification():
            return
        last = ''
        while True:
            time.sleep(self.delay)
            self.proxy = self.get_proxy(self.source)
            params = {'restriction': 'site ends with',
                      'host': '.' + self.domain,
                      'from': self.page_num}
            resp = self.get(self.addr + last, params)
            subdomains = self.match_subdomains(resp)
            if not subdomains:  # If the search does not find a subdomain, stop the search
                break
            self.subdomains.update(subdomains)
            if 'Next Page' not in resp.text:  # Stop searching when the next page does not appear on the search page
                break
            last = re.search(r'&last=.*' + self.domain, resp.text).group(0)
            self.page_num += self.per_page_num
            if self.page_num > 500:
                break

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
        query = NetCraft(domain)
        query.run()

    if __name__ == '__main__':
        run('example.com')