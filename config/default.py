# coding=utf-8
"""
Garuda default configuration
"""

import pathlib
import warnings

# Disable all warning messages
warnings.filterwarnings("ignore")

# Path setting
relative_directory = pathlib.Path(__file__).parent.parent  # Garuda code relative path
module_dir = relative_directory.joinpath('modules')  # Garuda module catalog
third_party_dir = relative_directory.joinpath('thirdparty')  # Tripartite Tool Catalog
data_storage_dir = relative_directory.joinpath('data')  # Data storage directory
result_save_dir = relative_directory.joinpath('results')  # Result save directory
temp_save_dir = result_save_dir.joinpath('temp')

# Garuda entry parameter settings
enable_check_version = True  # Open the latest version check
enable_brute_module = True  # Use blasting module (default True)
enable_dns_resolve = True  # Use DNS to resolve subdomains (default True)
enable_http_request = True  # Use HTTP request subdomain (default True)
enable_finder_module = True  # Turn on the finder module, and the subdomain will be found again from the response body and JS (default True)
enable_altdns_module = True  # Turn on the altdns module, and it will use the replacement technology to reorganize the subdomain and find the new subdomain again (default True)
enable_enrich_module = True  # Turn on the enrich module, it will enrich the information, such as ip's cdn, cidr, asn, org, addr and isp information
enable_banner_identify = True  # Open WEB fingerprint recognition module (default True)
enable_takeover_check = False  # Enable subdomain takeover risk check (default False)
# Optional parameter values are'small','medium','large'
http_request_port = 'small'  # HTTP request subdomain (default'small', detection port 80,443)
# Optional values of True and False respectively indicate export survival and all subdomain results
result_export_alive = False  # Export only the subdomain results that survive (default False)
# The optional format of the parameter is'csv','json'
result_save_format = 'csv'  # File format for saving subdomain results (default csv)
# The parameter path defaults to None and uses the Garuda result directory to automatically generate the path
result_save_path = None  # File path for saving subdomain results (default None)

# Collection module settings
save_module_result = False  # Save the findings of each module as a json file (default False)
enable_all_module = True  # Enable all collection modules (default True)
enable_partial_module = []  # To enable some collection modules, enable_all_module must be disabled to take effect
# Examples of collecting subdomains using only ask and baidu search engines
# enable_partial_module = ['modules.search.ask', 'modules.search.baidu']
module_thread_timeout = 90.0  # Timeout of each collection module thread (90 seconds by default)

# Blasting module settings
enable_wildcard_check = True  # Enable pan-analysis detection (default True)
enable_wildcard_deal = True  # Enable pan-analysis processing (default True)
brute_massdns_path = None  # Default None is automatically selected. If you need to fill in, please fill in the absolute path
brute_status_format = 'ansi'  # State output format when blasting (default asni, optional json)
brute_concurrent_num = 2000  # Number of concurrent queries (default 2000, maximum recommended 10000)
brute_socket_num = 1  # The number of sockets under each process at the time of blasting
brute_resolve_num = 15  # The number of recheck attempts to change the name server when the resolution fails
# The dictionary path used for blasting (default None uses data/subdomains.txt, please use the absolute path for custom dictionaries)
brute_wordlist_path = None
# The save path of the authoritative DNS name server of the domain name. When the domain name is enabled for pan-resolution, the name server will be used for A record query
authoritative_dns_path = data_storage_dir.joinpath('authoritative_dns.txt')
enable_recursive_brute = False  # Whether to use recursive blasting (default False)
brute_recursive_depth = 2  # Recursive blasting depth (default 2 layers)
# The dictionary path used to blast the next level of subdomains (default None uses data/subnames_next.txt, and the absolute path for custom dictionaries)
recursive_nextlist_path = None
enable_check_dict = False  # Whether to open the dictionary configuration check prompt (default False)
delete_generated_dict = True  # Whether to delete the temporarily generated dictionary during blasting (default True)
delete_massdns_result = True  # Whether to delete the analysis result output by massdns during blasting (default True)
only_save_valid = True  # Whether to store only the successfully resolved subdomains when processing the blasting results
check_time = 10  # Check the dictionary configuration dwell time (default 10 seconds)
enable_fuzz = False  # Whether to use fuzz mode to enumerate domain names
fuzz_place = None  # Specify the location of the blasting The specified location is represented by `@` Example: www.@.example.com
fuzz_rule = None  # Regular expression used in fuzz domain name Example:'[a-z][0-9]' means that the first digit is a letter and the second digit is a number
fuzz_list = None  # Dictionary path used by fuzz domain name
brute_ip_blacklist = {'0.0.0.0', '0.0.0.1'}  # IP blacklist If the subdomain resolves to the IP blacklist, it will be marked as an illegal subdomain
ip_appear_maximum = 100  # If multiple subdomains resolve to the same IP more than 100 times, they will be marked as illegal (pan resolution) subdomains

# altdns module settings
altdns_increase_num = True
altdns_decrease_num = True
altdns_replace_word = False
altdns_insert_word = False
altdns_add_word = False


# Banner recognition module settings
banner_process_number = 4  # Number of identification processes (default 4)

# Proxy settings
enable_request_proxy = False  # Whether to use proxy (global switch, default False)
proxy_all_module = False  # Proxy all modules
proxy_partial_module = ['GoogleQuery', 'AskSearch', 'DuckDuckGoSearch',
                        'GoogleAPISearch', 'GoogleSearch', 'YahooSearch',
                        'YandexSearch', 'CrossDomainXml',
                        'ContentSecurityPolicy']  # Agent custom module
request_proxy_pool = [{'http': 'http://127.0.0.1:1080',
                       'https': 'https://127.0.0.1:1080'}]  # Agent pool
# request_proxy_pool = [{'http': 'socks5h://127.0.0.1:10808',
#                        'https': 'socks5h://127.0.0.1:10808'}]  # Agent pool


# Request settings
request_thread_count = None  # The number of request threads (default None, automatically set according to the situation)
request_timeout_second = (13, 27)  # Request timeout seconds (default connect timout is recommended to be slightly greater than 3 seconds)
request_ssl_verify = False  # Request SSL verification (default False)
request_allow_redirect = True  # Request to allow redirection (default True)
request_redirect_limit = 10  # Request jump limit (default 10 times)
# Default request headers You can add custom request headers in headers
request_default_headers = {
    'Accept': 'text/html,application/xhtml+xml,'
              'application/xml;q=0.9,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
    'Cache-Control': 'max-age=0',
    'DNT': '1',
    'Referer': 'https://www.google.com/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                  '(KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',
    'Upgrade-Insecure-Requests': '1',
    'X-Forwarded-For': '127.0.0.1'
}
enable_random_ua = True  # Use random UA (default True, enable UA that can override request_default_headers)

# Search module settings
# Turning on full search will try to get all the results of the search engine search, but the search may take too long
enable_full_search = False  # Enable full search (default False)
enable_recursive_search = False  # Search subdomains recursively (default False)
search_recursive_times = 2  # Number of recursive search layers (default 2)

# DNS resolution settings
resolver_nameservers = [
    '223.5.5.5',  # AliDNS
    '119.29.29.29',  # DNSPod
    '114.114.114.114',  # 114DNS
    '8.8.8.8',  # Google DNS
    '1.1.1.1'  # CloudFlare DNS
]  # Specify the DNS name server for query
resolver_timeout = 5.0  # Parsing timeout (default 5.0 seconds)
resolver_lifetime = 10.0  # Parsing time to live (default 10.0 seconds)

# Request port detection settings
# You can add a custom port to the port list
small_ports = [80, 443]  # Used by default
medium_ports = [80, 443, 8000, 8080, 8443]
# Note: It is recommended not to use a large port range for the domain name of a large factory, because there are too many subdomains of a large factory, and the use of a large port range will result in the generation
# Requests in the order of 100,000, millions, and tens of millions may cause the out-of-memory program to crash. In addition, the waiting time for requests of this level is long.
# Garuda is not a port scanning tool. If you want to scan ports, it is recommended to use tools such as nmap and zmap.
large_ports = [80, 81, 280, 300, 443, 591, 593, 832, 888, 901, 981, 1010, 1080,
               1100, 1241, 1311, 1352, 1434, 1521, 1527, 1582, 1583, 1944, 2082,
               2082, 2086, 2087, 2095, 2096, 2222, 2301, 2480, 3000, 3128, 3333,
               4000, 4001, 4002, 4100, 4125, 4243, 4443, 4444, 4567, 4711, 4712,
               4848, 4849, 4993, 5000, 5104, 5108, 5432, 5555, 5800, 5801, 5802,
               5984, 5985, 5986, 6082, 6225, 6346, 6347, 6443, 6480, 6543, 6789,
               7000, 7001, 7002, 7396, 7474, 7674, 7675, 7777, 7778, 8000, 8001,
               8002, 8003, 8004, 8005, 8006, 8008, 8009, 8010, 8014, 8042, 8069,
               8075, 8080, 8081, 8083, 8088, 8090, 8091, 8092, 8093, 8016, 8118,
               8123, 8172, 8181, 8200, 8222, 8243, 8280, 8281, 8333, 8384, 8403,
               8443, 8500, 8530, 8531, 8800, 8806, 8834, 8880, 8887, 8888, 8910,
               8983, 8989, 8990, 8991, 9000, 9043, 9060, 9080, 9090, 9091, 9200,
               9294, 9295, 9443, 9444, 9800, 9981, 9988, 9990, 9999, 10000,
               10880, 11371, 12043, 12046, 12443, 15672, 16225, 16080, 18091,
               18092, 20000, 20720, 24465, 28017, 28080, 30821, 43110, 61600]
ports = {'small': small_ports, 'medium': medium_ports, 'large': large_ports}

common_subnames = {'i', 'w', 'm', 'en', 'us', 'zh', 'w3', 'app', 'bbs',
                   'web', 'www', 'job', 'docs', 'news', 'blog', 'data',
                   'help', 'live', 'mall', 'blogs', 'files', 'forum',
                   'store', 'mobile'}

# Module API configuration
# Censys can register for free to get the API: https://censys.io/api
censys_api_id = ''
censys_api_secret = ''

# Binaryedge can register for free to get the API: https://app.binaryedge.io/account/api
# The free API is valid for only 1 month, and can be regenerated after expiration, and it can be inquired 250 times per month.
binaryedge_api = ''

# Chinaz can register for free to get the API: http://api.chinaz.com/ApiDetails/Alexa
chinaz_api = ''

# Bing can register for free to get the API: https://azure.microsoft.com/zh-cn/services/
# cognitive-services/bing-web-search-api/#web-json
bing_api_id = ''
bing_api_key = ''

# SecurityTrails can register for free to get the API: https://securitytrails.com/corp/api
securitytrails_api = ''

# https://fofa.so/api
fofa_api_email = ''  # fofa user mailbox
fofa_api_key = ''  # fofa user key

# Google can register for free to get the API:
# The free API can only query the first 100 results
# https://developers.google.com/custom-search/v1/overview#search_engine_id
# After creating a custom search engine, you need to enable Search the entire web on the responding control panel
google_api_id = ''  # Google API custom search engine id
# https://developers.google.com/custom-search/v1/overview#api_key
google_api_key = ''  # Google API自定义搜索key

# https://api.passivetotal.org/api/docs/
riskiq_api_username = ''
riskiq_api_key = ''

# Shodan can register for free to get the API: https://account.shodan.io/register
# Free API speed limit query once per second
shodan_api_key = ''
# ThreatBook API querying subdomains requires a fee https://x.threatbook.cn/nodev4/vb4/myAPI
threatbook_api_key = ''

# VirusTotal can register for free to get the API: https://developers.virustotal.com/reference
virustotal_api_key = ''

# https://www.zoomeye.org/doc?channel=api
zoomeye_api_usermail = ''
zoomeye_api_password = ''

# Spyse can register for free to get the API: https://spyse.com/
spyse_api_token = ''

# https://www.circl.lu/services/passive-dns/
circl_api_username = ''
circl_api_password = ''

# https://www.dnsdb.info/
dnsdb_api_key = ''

# ipv4info can register for free to get the API: http://ipv4info.com/tools/api/
# The free API is valid for only 2 days, and it can be regenerated after expiration, and it can be queried 50 times a day.
ipv4info_api_key = ''

# https://github.com/360netlab/flint
# passivedns_api_addr is empty by default and uses http://api.passivedns.cn
# passivedns_api_token can be empty
passivedns_api_addr = ''
passivedns_api_token = ''

# Github Token can be generated by visiting https://github.com/settings/tokens, user is the Github username
# Used for subdomain takeover and subdomain collection
github_api_user = ''
github_api_token = ''

# obtain Cloudflare API key from https://dash.cloudflare.com/profile/api-tokens
cloudflare_api_token = ''
