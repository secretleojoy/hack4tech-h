"""
Query the NS record of the domain name (domain name server record, record which domain name server resolves the domain name), and check whether the found domain name server is
Whether to enable DNS domain transfer, if it is enabled and without access control and authentication, use it to obtain all the records of the domain name.

DNS zone transfer refers to a backup domain name server using data from the primary domain name server to refresh itself
The purpose of the domain database is to make redundant backups to prevent DNS resolution from being unavailable when the primary domain name server fails.
This vulnerability can be exploited when the primary server turns on DNS domain transmission and at the same time does not perform access control and authentication on the standby server that comes in the request.
Get all the records of a certain domain.
"""
import dns.resolver
import dns.zone

from common import utils
from common.check import Check
from config.log import logger


class AXFR(Check):
    def __init__(self, domain):
        Check.__init__(self)
        self.domain = domain
        self.module = 'check'
        self.source = 'AXFRCheck'
        self.results = []

    def axfr(self, server):
        """
        Perform domain transfer

        :param server: domain server
        """
        logger.log('DEBUG', f'Trying to perform domain transfer in {server} '
                            f'of {self.domain}')
        try:
            xfr = dns.query.xfr(where=server, zone=self.domain,
                                timeout=5.0, lifetime=10.0)
            zone = dns.zone.from_xfr(xfr)
        except Exception as e:
            logger.log('DEBUG', e.args)
            logger.log('DEBUG', f'Domain transfer to server {server} of '
                                f'{self.domain} failed')
            return
        names = zone.nodes.keys()
        for name in names:
            full_domain = str(name) + '.' + self.domain
            subdomain = self.match_subdomains(full_domain)
            self.subdomains.update(subdomain)
            record = zone[name].to_text(name)
            self.results.append(record)
        if self.results:
            logger.log('DEBUG', f'Found the domain transfer record of '
                                f'{self.domain} on {server}')
            logger.log('DEBUG', '\n'.join(self.results))
            self.results = []

    def check(self):
        """
        check
        """
        resolver = utils.dns_resolver()
        try:
            answers = resolver.query(self.domain, "NS")
        except Exception as e:
            logger.log('ERROR', e.args)
            return
        nsservers = [str(answer) for answer in answers]
        if not len(nsservers):
            logger.log('ALERT', f'No name server record found for {self.domain}')
            return
        for nsserver in nsservers:
            self.axfr(nsserver)

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
    check = AXFR(domain)
    check.run()


if __name__ == '__main__':
    run('ZoneTransfer.me')
    # run('example.com')
