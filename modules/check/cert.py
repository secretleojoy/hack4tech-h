"""
Check the domain name certificate to collect subdomains
"""
import socket
import ssl

from config.log import logger
from common.check import Check


class CertInfo(Check):
    def __init__(self, domain):
        Check.__init__(self)
        self.domain = domain
        self.module = 'check'
        self.source = 'CertInfo'

    def check(self):
        """
        Obtain a domain name certificate and match the subdomain name in the certificate
        """
        try:
            ctx = ssl.create_default_context()
            sock = socket.socket()
            sock.settimeout(10)
            wrap_sock = ctx.wrap_socket(sock, server_hostname=self.domain)
            wrap_sock.connect((self.domain, 443))
            cert_dict = wrap_sock.getpeercert()
        except Exception as e:
            logger.log('DEBUG', e.args)
            return
        subdomains = self.match_subdomains(str(cert_dict))
        self.subdomains.update(subdomains)

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
    check = CertInfo(domain)
    check.run()


if __name__ == '__main__':
    run('example.com')
