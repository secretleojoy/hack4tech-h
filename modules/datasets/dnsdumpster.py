from common.query import Query


class DNSDumpster(Query):
    def __init__(self, domain):
        Query.__init__(self)
        self.domain = domain
        self.module = 'Dataset'
        self.source = "DNSDumpsterQuery"
        self.addr = 'https://dnsdumpster.com/'

    def query(self):
        """
        Query the subdomain from the interface and do subdomain matching
                 """
        self.header = self.get_header()
        self.header.update({'Referer': 'https://dnsdumpster.com'})
        self.proxy = self.get_proxy(self.source)
        resp = self.get(self.addr)
        if not resp:
            return
        self.cookie = resp.cookies
        data = {'csrfmiddlewaretoken': self.cookie.get('csrftoken'),
                'targetip': self.domain}
        resp = self.post(self.addr, data)
        self.subdomains = self.collect_subdomains(resp)

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
        query = DNSDumpster(domain)
        query.run()

    if __name__ == '__main__':
        run('mi.com')