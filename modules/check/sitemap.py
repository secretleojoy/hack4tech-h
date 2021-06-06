"""
Check the content security policy Collect subdomains Collect subdomains
"""
from common.check import Check


class Sitemap(Check):
    def __init__(self, domain):
        Check.__init__(self)
        self.domain = domain
        self.module = 'check'
        self.source = 'SitemapCheck'

    def check(self):
        """
        Regularly matches the subdomain in the sitemap file of the domain name
        """
        filenames = {'sitemap.xml', 'sitemap.txt', 'sitemap.html', 'sitemapindex.xml'}
        self.to_check(filenames)

    def run(self):
        """
        Class execution entry
        """
        self.begin()
        self.check()
        self.finish()
        self.save_json()
        self.gen_result()
        self.save_db()


def run(domain):
    """
    Class uniform call entry

    :param str domain: domain name
    """
    check = Sitemap(domain)
    check.run()


if __name__ == '__main__':
    run('qq.com')
