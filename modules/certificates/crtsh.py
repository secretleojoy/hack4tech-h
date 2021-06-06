from common.query import Query


class Crtsh(Query):
    def __init__(self, domain):
        Query.__init__(self)
        self.domain = domain
        self.module = 'Certificate'
        self.source = 'CrtshQuery'
        self.addr = 'https://crt.sh/'

    def query(self):
        """
        Query the subdomain from the interface and do subdomain matching
        """
        self.header = self.get_header()
        self.proxy = self.get_proxy(self.source)
        params = {'q': f'%.{self.domain}', 'output': 'json'}
        resp = self.get(self.addr, params)
        if not resp:
            return
        text = resp.text.replace(r'\n', ' ')
        subdomains = self.match_subdomains(text)
        self.subdomains.update(subdomains)

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
    query = Crtsh(domain)
    query.run()


if __name__ == '__main__':
    run('example.com')
