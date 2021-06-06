from config import settings
from common.query import Query
from config.log import logger


class CensysAPI(Query):
    def __init__(self, domain):
        Query.__init__(self)
        self.domain = domain
        self.module = 'Certificate'
        self.source = "CensysAPIQuery"
        self.addr = 'https://www.censys.io/api/v1/search/certificates'
        self.id = settings.censys_api_id
        self.secret = settings.censys_api_secret
        self.delay = 3.0  # Censys interface query rate limit as fast as 2.5 seconds to check once

    def query(self):
        """
        Query the subdomain from the interface and do subdomain matching
        """
        self.header = self.get_header()
        self.proxy = self.get_proxy(self.source)
        data = {
            'query': f'parsed.names: {self.domain}',
            'page': 1,
            'fields': ['parsed.subject_dn', 'parsed.names'],
            'flatten': True}
        resp = self.post(self.addr, json=data, auth=(self.id, self.secret))
        if not resp:
            return
        json = resp.json()
        status = json.get('status')
        if status != 'ok':
            logger.log('ALERT', f'{self.source} module {status}')
            return
        subdomains = self.match_subdomains(resp.text)
        self.subdomains.update(subdomains)
        pages = json.get('metadata').get('pages')
        for page in range(2, pages + 1):
            data['page'] = page
            resp = self.post(self.addr, json=data, auth=(self.id, self.secret))
            self.subdomains = self.collect_subdomains(resp)

    def run(self):
        """
        Class execution entry
        """
        if not self.have_api(self.id, self.secret):
            return
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
    query = CensysAPI(domain)
    query.run()


if __name__ == '__main__':
    run('example.com')
