from config import settings
from common.module import Module


class Search(Module):
    """
    Search base class
    """
    def __init__(self):
        Module.__init__(self)
        self.page_num = 0  # To display the starting number of the search
        self.per_page_num = 50  # Display the number of searches per page
        self.recursive_search = settings.enable_recursive_search
        self.recursive_times = settings.search_recursive_times
        self.full_search = settings.enable_full_search

    @staticmethod
    def filter(domain, subdomain):
        """
        Generate search filter statements
        Use the -site: grammar supported by search engines to filter out subdomains with many search pages to discover new domains

        :param str domain: domain name
        :param set subdomain: Collection of subdomains
        :return: Filter statement
        :rtype: str
        """
        statements_list = []
        subdomains_temp = set(map(lambda x: x + '.' + domain, settings.common_subnames))
        subdomains_temp = list(subdomain.intersection(subdomains_temp))
        for i in range(0, len(subdomains_temp), 2):  # Exclude 2 subdomains at the same time
            statements_list.append(''.join(set(map(lambda s: ' -site:' + s,
                                                   subdomains_temp[i:i + 2]))))
        return statements_list

    def match_location(self, url):
        """
        URL after matching the jump
        For some search engines (such as Baidu search), the display URL is incomplete when searching for it
        This function will send a head request to each result link to obtain the location value of the response header and do subdomain matching

        :param str url: URL link to display the result
        :return: Matched subdomain
        :rtype set
        """
        resp = self.head(url, check=False, allow_redirects=False)
        if not resp:
            return set()
        location = resp.headers.get('location')
        if not location:
            return set()
        return set(self.match_subdomains(location))

    def check_subdomains(self, subdomains):
        """
        Check whether the searched subdomain results meet the conditions

        :param subdomains: Subdomain result
        :return:
        """
        if not subdomains:
            # If no subdomain is found in the search, stop the search
            return False
        if not self.full_search and subdomains.issubset(self.subdomains):
            # During the full search process, if the search results are completely duplicated, stop the search
            return False
        return True

    def recursive_subdomain(self):
        # Recursively search the subdomains of the next layer
        # Starting from 1, we have done a layer 1 subdomain search before, and the current actual number of recursive layers is layer+1
        for layer_num in range(1, self.recursive_times):
            for subdomain in self.subdomains:
                # Restrictions for the next level of subdomain search
                count = subdomain.count('.') - self.domain.count('.')
                if count == layer_num:
                    yield subdomain
