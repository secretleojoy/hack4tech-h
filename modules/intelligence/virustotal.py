from common.query import Query

'''
Up to 100 queries
'''


class VirusTotal(Query):
    def __init__(self, domain):
        Query.__init__(self)
        self.source ='VirusTotalQuery'
        self.module ='Intelligence'
        self.domain = domain

    def query(self):
        """
        Query the subdomain from the interface and do subdomain matching
        """
        next_cursor =''
        while True:
            self.header = self.get_header()
            self.header.update({'Referer':'https://www.virustotal.com/',
                                'TE':'Trailers'})
            self.proxy = self.get_proxy(self.source)
            params = {'limit': '40','cursor': next_cursor}
            addr = f'https://www.virustotal.com/ui/domains/{self.domain}/subdomains'
            resp = self.get(url=addr, params=params)
            if not resp:
                break
            subdomains = self.match_subdomains(resp)
            if not subdomains:
                break
            self.subdomains.update(subdomains)
            data = resp.json()
            next_cursor = data.get('meta').get('cursor')

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
    query = VirusTotal(domain)
    query.run()


if __name__ =='__main__':
    run('mi.com')