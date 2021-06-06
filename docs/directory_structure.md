```
D:.
| .gitignore
| .travis.yml
| brute.py subdomain blasting module that can be run separately
| collect.py Upper call of each collection module
| dbexport.py A database export module that can be run separately
| Dockerfile
| LICENSE
| garuda.py Garuda main entrance
| Pipfile
| Pipfile.lock
| README.en.md
| README.md
| requirements.txt
| takeover.py subdomain interface risk check module that can be run separately
| _config.yml
|
+---.github
| +---ISSUE_TEMPLATE
| | bug_report.md
| | bug_report_zh.md
| | custom.md
| | feature_request.md
| |
| \---workflows
| test.yml
|
|
+---common common call module
| crawl.py
| database.py
| domain.py
| lookup.py
| module.py
| query.py
| request.py
| resolve.py
| search.py
| utils.py
| __init__.py
|
+---config configuration directory
| api.py Part of the API configuration file of the collection module
| log.py Log module configuration file
| setting.py Garuda main configuration file
|
+---data store some required data
| authoritative_dns.txt temporarily stores the IP address of the authoritative DNS name server with the pan-resolution domain name enabled
| subnames_big.7z Subdomain blasting super large dictionary
| nameservers_cn.txt Chinese mainstream name server IP address
| fingerprints.json Check fingerprints for subdomain takeover risk
| nameservers.txt Global mainstream name server IP address
| subnames_next.txt The next subdomain dictionary
| public_suffix_list.dat top-level domain suffix
| srv_prefixes.json Common SRV record prefix names
| subnames.txt subdomain blasting common dictionary
|
+---docs Related documents
| changes.md
| collection_modules.md
| contributors.md
| installation_dependency.md
| todo.md
| troubleshooting.md
| usage_example.svg
| usage_help.en.md
| usage_help.md
|
+---images
| Database.png
| Donate.png
| Result.png
|
+---modules
| +---autotake automatically take over the module
| | github.py
| |
| +---certificates Use certificate transparency to collect subdomain modules
| | censys_api.py
| | certspotter.py
| | crtsh.py
| | entrust.py
| | google.py
| | spyse_api.py
| |
| +---check Regular check collection subdomain module
| | axfr.py
| | cdx.py
| | cert.py
| | csp.py
| | robots.py
| | sitemap.py
| |
| +---crawl Use web crawler files to collect subdomain modules
| | archivecrawl.py
| | commoncrawl.py
| |
| +---datasets Collect subdomain modules using DNS data sets
| | binaryedge_api.py
| | bufferover.py
| | cebaidu.py
| | chinaz.py
| | chinaz_api.py
| | circl_api.py
| | dnsdb_api.py
| | dnsdumpster.py
| | hackertarget.py
| | ip138.py
| | ipv4info_api.py
| | netcraft.py
| | passivedns_api.py
| | ptrarchive.py
| | qianxun.py
| | rapiddns.py
| | riddler.py
| | robtex.py
| | securitytrails_api.py
| | sitedossier.py
| | threatcrowd.py
| | wzpc.py
| | ximcx.py
| |
| +---dnsquery Use DNS query to collect subdomain module
| | mx.py
| | ns.py
| | soa.py
| | srv.py
| | txt.py
| |
| +---intelligence uses threat intelligence platform data collection subdomain module
| | alienvault.py
| | riskiq_api.py
| | threatbook_api.py
| | threatminer.py
| | virustotal.py
| | virustotal_api.py
| |
| \---search Use search engines to discover subdomain modules
| ask.py
| baidu.py
| bing.py
| bing_api.py
| exalead.py
| fofa_api.py
| gitee.py
| github_api.py
| google.py
| google_api.py
| shodan_api.py
| so.py
| sogou.py
| yahoo.py
| yandex.py
| zoomeye_api.py
|
+---results result directory
+---test test directory
| example.py
|
\---thirdparty stores the third party tools to be called
    \---massdns
        | LICENSE
        | massdns_darwin_x86_64
        | massdns_linux_i686
        | massdns_linux_x86_64
        | README.md
        |
        \---windows
            +---x64
            | cygwin1.dll
            | massdns_windows_amd64.exe
            |
            \---x86
                    cyggcc_s-1.dll
                    cygwin1.dll
                    massdns_windows_i686.exe
```
