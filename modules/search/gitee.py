import time
from bs4 import BeautifulSoup
from common.search import Search
from config.log import logger


class Gitee(Search):
    def __init__(self, domain):
        Search.__init__(self)
        self.source = 'GiteeSearch'
        self.module = 'Search'
        self.addr = 'https://search.gitee.com/'
        self.domain = domain

    def search(self):
        """
        Query the subdomain from the interface and do subdomain matching
                """
        page_num = 1
        while True:
            time.sleep(self.delay)
            self.header = self.get_header()
            self.proxy = self.get_proxy(self.source)
            params = {'pageno': page_num, 'q': self.domain, 'type': 'code'}
            try:
                resp = self.get(self.addr, params=params)
            except Exception as e:
                logger.log('ERROR', e.args)
                break
            if not resp:
                break
            if resp.status_code != 200:
                logger.log('ERROR', f'{self.source} module query failed')
                break
            if 'class="empty-box"' in resp.text:
                break
            soup = BeautifulSoup(resp.text, 'html.parser')
            subdomains = self.match_subdomains(soup, fuzzy=False)
            if not self.check_subdomains(subdomains):
                break
            self.subdomains.update(subdomains)
            if '<li class="disabled"><a href="###">' in resp.text:
                break
            page_num += 1
            if page_num >= 100:
                break

        def run(self):
            """
            Class execution entry
            """
            self.begin()
            self.search()
            self.finish()
            self.save_json()
            self.gen_result()
            self.save_db()

    def run(domain):
        """
        Class uniform call entry

        :param str domain: domain name
        """
        query = Gitee(domain)
        query.run()

    if __name__ == '__main__':
        run('qq.com')