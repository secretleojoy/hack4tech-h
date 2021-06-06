import cdx_toolkit
from common.crawl import Crawl
from config.log import logger


class ArchiveCrawl(Crawl):
    def __init__(self, domain):
        Crawl.__init__(self)
        self.domain = domain
        self.module = 'Crawl'
        self.source = 'ArchiveCrawl'

    def crawl(self, domain, limit):
        """

        :param domain:
        :param limit:
        """
        self.header = self.get_header()
        self.proxy = self.get_proxy(self.source)
        cdx = cdx_toolkit.CDXFetcher(source='ia')
        url = f'*.{domain}/*'
        size = cdx.get_size_estimate(url)
        logger.log('DEBUG', f'{url} ArchiveCrawl size estimate {size}')

        for resp in cdx.iter(url, limit=limit):
            if resp.data.get('status') not in ['301', '302']:
                url = resp.data.get('url')
                subdomains = self.match_subdomains(domain, url + resp.text)
                self.subdomains.update(subdomains)

    def run(self):
        """
        Class execution entry
        """
        self.begin()
        self.crawl(self.domain, 50)
        # Crawl the discovered subdomains to discover new subdomains
        for subdomain in self.subdomains:
            if subdomain != self.domain:
                self.crawl(subdomain, 10)
        self.finish()
        self.save_json()
        self.gen_result()
        self.save_db()


def run(domain):
    """
    Class uniform call entry

    :param str domain: domain name
    """
    crawl = ArchiveCrawl(domain)
    crawl.run()


if __name__ == '__main__':
    run('example.com')
