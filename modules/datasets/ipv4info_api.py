from config import settings
from common.query import Query
from config.log import logger


class IPv4InfoAPI(Query):
    def __init__(self, domain):
        Query.__init__(self)
        self.domain = domain
        self.module = 'Dataset'
        self.source = 'IPv4InfoAPIQuery'
        self.addr = ' http://ipv4info.com/api_v1/'
        self.api = settings.ipv4info_api_key

    def query(self):
        """
        Query the subdomain from the interface and do subdomain matching
                """
        page = 0
        while True:
            self.header = self.get_header()
            self.proxy = self.get_proxy(self.source)
            params = {'type': 'SUBDOMAINS', 'key': self.api,
                      'value': self.domain, 'page': page}
            resp = self.get(self.addr, params)
            if not resp:
                return
            if resp.status_code != 200:
                break  # The request is abnormal. Usually there is a problem with the network, so the request will not be continued.
            try:
                json = resp.json()
            except Exception as e:
                logger.log('DEBUG', e.args)
                break
            subdomains = self.match_subdomains(str(json))
            if not subdomains:
                break
            self.subdomains.update(subdomains)
            # Do not use subdomains directly because there may be subdomains that do not meet the standard
            subdomains = json.get('Subdomains')
            if subdomains and len(subdomains) < 300:
                # The ipv4info subdomain query interface returns a maximum of 300 each time, which is used to determine whether there is a next page
                break
            page += 1
            if page >= 50:  # ipv4info subdomain query interface allows querying up to 50 pages
                break

    def run(self):
        """
        Class execution entry
        """
        if not self.have_api(self.api):
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
        query = IPv4InfoAPI(domain)
        query.run()

    if __name__ == '__main__':
        run('example.com')