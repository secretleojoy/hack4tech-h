# coding=utf-8
"""
Garuda
"""

import pathlib
import urllib3

# path setting
relative_directory = pathlib.Path(__file__).parent.parent  # Garuda path
module_dir = relative_directory.joinpath('modules')  # garuda link
third_party_dir = relative_directory.joinpath('thirdparty')  # thirdpaty
data_storage_dir = relative_directory.joinpath('data')  # MySQL data base takeover
result_save_dir = relative_directory.joinpath('results')  # Result save directory

# Garuda entry parameter settings
enable_dns_resolve = True  # Use DNS to resolve subdomains (default True)
enable_http_request = True  # Use HTTP request subdomain (default True)
enable_takeover_check = False  # Enable subdomain takeover risk check (defaultFalse)
# Optional values for parameter port are 'default', 'small', 'large'
http_request_port = 'default'  # HTTP request subdomain (default 'default', detect port 80)
# Optional value of parameter alive is True and False respectively indicate export survival, all subdomain results
result_export_alive = True  # Export only the subdomain results that survive (default False)
# The optional format of the parameter format is 'rst', 'csv', 'tsv', 'json', 'yaml', 'html',
# 'jira', 'xls', 'xlsx', 'dbf', 'latex', 'ods'
result_save_format = 'csv'  # File format for saving subdomain results (default csv)
# File format for saving subdomain results (default csv
result_save_path = None  # File path for saving subdomain results (default None)

# File path for saving subdomain results (default None
save_module_result = False  # fale)
enable_all_module = True  # Enable all modules (default True)
enable_partial_module = []  # To enable some modules, enable_all_module must be disabled to take effect
# Examples of collecting subdomains using only ask and baidu search engines
# enable_partial_module = [('modules.search', 'ask')
#                          ('modules.search', 'baidu')]
module_thread_timeout = 180.0  # Timeout time of each collection module thread (default 3 minutes)

# Blasting module settings
enable_brute_module = True  # Use blasting module (default False)
enable_wildcard_check = True  # Enable pan-analysis detection (default True)
enable_wildcard_deal = True  # Enable pan-analysis processing (default True)
brute_massdns_path = None  # Default None is automatically selected. If you need to fill in,
brute_status_format = 'ansi'  # State output format when blasting (default asni, optional json）
# The number of processes used in blasting (set according to the number of CPUs in the computer, should not be greater than the number of logical CPUs)
brute_process_num = 1  #  1

brute_concurrent_num = 10000  #
brute_socket_num = 1  # The number of sockets under each process at the time of blasting
brute_resolve_num = 50  # The number of recheck attempts to change the name server when the resolution fails
# The dictionary path used by blasting Default data/subdomains.txt
brute_wordlist_path = data_storage_dir.joinpath('subnames.txt')
brute_nameservers_path = data_storage_dir.joinpath('cn_nameservers.txt')
# The save path of the authoritative DNS name server of the domain name. When the domain name is turned on, the name server will be used for A record query
authoritative_dns_path = data_storage_dir.joinpath('authoritative_dns.txt')
enable_recursive_brute = False  # Whether to use recursive blasting (default False)
brute_recursive_depth = 2  # Recursive blasting depth (default 2 layers)
# The dictionary path used to blast the next level of subdomains Default data/next_subdomains.txt
recursive_nextlist_path = data_storage_dir.joinpath('next_subnames.txt')
enable_check_dict = False  # Whether to open the dictionary configuration check prompt (default False)
delete_generated_dict = True  # Whether to delete the temporarily generated dictionary during blasting (default True)
# Whether to delete the analysis result output by massdns during blasting (default True)
# The massdns output contains more detailed analysis results
#  Note: When the blasted dictionary is large or recursive blasting is used, or the target domain name has pan-resolution, the generated file may be very large
delete_massdns_result = True
only_save_valid = True  # Whether to store only the successfully resolved subdomains when processing the blasting results
check_time = 10  # Check the dictionary configuration dwell time (default 10 seconds)
enable_fuzz = False  # Whether to use fuzz mode to enumerate domain names
fuzz_place = None  # Specify the location of the blasting The specified location is represented by `@` Example: www.@.example.com
fuzz_rule = None  # Regular fuzz domain name Example:'[a-z][0-9]' means that the first digit is a letter and the second digit is a number
brute_ip_blacklist = {'0.0.0.0', '0.0.0.1'}  # IP blacklist If the subdomain resolves to the IP blacklist, it will be marked as an illegal subdomain
ip_appear_maximum = 100  # If multiple subdomains resolve to the same IP more than 100 times, they will be marked as illegal (pan resolution) subdomains

# Proxy settings
enable_proxy = False  # Whether to use proxy (global switch)
proxy_all_module = False  # Proxy all modules
proxy_partial_module = ['GoogleQuery', 'AskSearch', 'DuckDuckGoSearch',
                        'GoogleAPISearch', 'GoogleSearch', 'YahooSearch',
                        'YandexSearch', 'CrossDomainXml',
                        'ContentSecurityPolicy']  # Agent custom module
proxy_pool = [{'http': 'http://127.0.0.1:1080',
               'https': 'https://127.0.0.1:1080'}]  # Agent pool
# proxy_pool = [{'http': 'socks5h://127.0.0.1:10808',
#                'https': 'socks5h://127.0.0.1:10808'}]  # Agent pool


# Network request settings
enable_fake_header = True  # Enable forged request headers
request_delay = 1  # Request delay
request_timeout = 80  # Request timed out
request_verify = False  # Request SSL verification
# Disable security warning messages
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Search module settings
enable_recursive_search = False  # Recursive search for subdomains
search_recursive_times = 2  # Recursive search level

# DNS resolution settings
resolve_coroutine_num = 64
resolver_nameservers = [
    '223.5.5.5',  # AliDNS
    '119.29.29.29',  # DNSPod
    '114.114.114.114',  # 114DNS
    '8.8.8.8',  # Google DNS
    '1.1.1.1'  # CloudFlare DNS
]  # Specify the DNS name server for query
resolver_timeout = 5.0  # server
resolver_lifetime = 60.0  # Analyze time to live
limit_resolve_conn = 500  # Limit the number of parsing at the same time (default 500)

# Request port detection settings
# You can add a custom port to the port list
default_ports = [443]  # Used by default
small_ports = [80, 443, 8000, 8080, 8443]
# Note: It is recommended not to use a large port range for the domain name of a large factory, because there are too many subdomains of a large factory, and the use of a large port range will cause
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
ports = {'default': default_ports, 'small': small_ports, 'large': large_ports}

# aiohttp related configuration
verify_ssl = False
# aiohttp supports HTTP/HTTPS proxy
aiohttp_proxy = None  # proxy="http://user:pass@some.proxy.com"
allow_redirects = True  # Allow request jump
fake_header = True  # Use forged request headers
# Use
# The request_method can only be HEAD or GET, the HEAD request method is faster, but the response body cannot be retrieved and extracted from it
request_method = 'GET'  # Use request method, default GET
sockread_timeout = 10  # Each request socket read timeout time, the default is 5 seconds
sockconn_timeout = 10  # Each request socket connection timeout time, the default is 5 seconds
# Limit the total number of connections opened at the same time
limit_open_conn = 100  # Default 100
# Limit the number of connections opened on the same endpoint at the same time ((host, port, is_ssl) 3 are the same)
limit_per_host = 10  # 0 means no limit, default 10

subdomains_common = {'i', 'w', 'm', 'en', 'us', 'zh', 'w3', 'app', 'bbs',
                     'web', 'www', 'job', 'docs', 'news', 'blog', 'data',
                     'help', 'live', 'mall', 'blogs', 'files', 'forum',
                     'store', 'mobile'}
