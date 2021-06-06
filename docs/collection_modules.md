# Collection module description #

If you want to use the module that collects subdomains through API, please go to [api.py](../config/api.py) to configure relevant information first. Most platform APIs can be obtained for free by registering an account.

If you specify to use certain modules, you can set it in [api.py](../config/api.py):

```python
enable_all_module = False  # Do not open all modules
enable_partial_module = [('modules.search', 'ask'), ('modules.search', 'baidu')]  # Only use ask and baidu search engines to collect subdomains
```

If you specify to use certain modules to use the proxy, you can set it in [api.py](../config/api.py):

```python
enable_proxy = True  # Use proxy
proxy_all_module = False  # Do not proxy all modules
proxy_partial_module = ['GoogleQuery', 'AskSearch']  # Only proxy GoogleQuery and AskSearch modules (source attribute value of each module)
```

The following is the description of each module:The following is the description of each module:

 1. Use certificate transparency to collect subdomains (currently there are 6 modules:`censys_api`，`certdb_api`，`certspotter`，`crtsh`，`entrust`，`google`）
  | Module name | Do you need a proxy | Do you need an API | Other instructions |
       | ----------- | ------------ | ----------- | ------------ -------------------------------------- |
       | censys_api | No | Yes | Please refer to [api.py](../config/api.py) for API usage and application |
       | certspotter | No | No | |
       | crtsh | No | No | |
       | entrust | No | No | |
       | google | yes | no | |
       | spyse_api | No | Yes | Please refer to [api.py](../config/api.py) for API usage and application |


  2. Routine checks to collect subdomains (currently there are 4 modules: domain transfer vulnerability exploit `axfr`, check cross-domain policy file `cdx`, check HTTPS certificate `cert`, check content security policy `csp`, check will be added later NSEC records, NSEC3 records and other modules)

       | Module name | Do you need a proxy | Do you need an API | Other instructions |
       | -------- | ---------------------- | ----------- | ----- ------------- |
       | axfr | No | No | Domain Transfer Vulnerability Exploitation |
       | cdx | Manual setting (not used by default) | No | Check the cross-domain policy file |
       | cert | No | No | Check HTTPS certificate |
       | csp | Manual setting (not used by default) | No | Check content security policy |
       | robots | Manual setting (not used by default) | No | Check the robots.txt file |
       | sitemap | Manual setting (not used by default) | No | Check sitemap file |
  3. Use online crawler archives to collect subdomains (currently there are 2 modules: `archivecrawl`, `commoncrawl`, this module is still being debugged, this module needs to be added and improved)

       | Module name | Do you need a proxy | Do you need an API | Other instructions |
       | ------------ | ------------ | ----------- | -------- |
       | archivecrawl | No | No | |
       | commoncrawl | No | No | |

  4. Use DNS data set to collect subdomains (currently there are 24 modules: `cebaidu`, `binaryedge_api`, `circl_api`, `cloudflare`, `hackertarget`, `riddler`, `bufferover`, `dnsdb`, `ipv4info `, `robtex`, `chinaz`, `dnsdb_api`, `netcraft`, `securitytrails_api`, `chinaz_api`, `dnsdumpster`, `passivedns_api`, `ptrarchive`, `sitedossier`,`threatcrowd`)

      | Module name | Do you need a proxy | Do you need an API | Other instructions |
      | ------------------ | ------------ | ----------- | ----- --------------------------------------------- |
      | binaryedge_api | No | Yes | Please refer to [api.py](../config/api.py) for API usage and application |
      | bufferover | No | No | |
      | cebaidu | No | No | |
      | chinaz | No | No | |
      | chinaz_api | No | Yes | Please refer to [api.py](../config/api.py) for API usage and application |
      | circl_api | No | Yes | Please refer to [api.py](../config/api.py) for API usage and application |
      | cloudflare_api | No | Yes | Please refer to [api.py](../config/api.py) for API usage and application |
      | dnsdb | No | No | |
      | dnsdb_api | No | Yes | Please refer to [api.py](../config/api.py) for API usage and application |
      | dnsdumpster | No | No | |
      | hackertarget | No | No | |
      | ip138 | No | No | |
      | ipv4info | No | Yes | Please refer to [api.py](../config/api.py) for API usage and application |
      | netcraft | No | No | |
      | passivedns_api | No | Yes | Please refer to [api.py](../config/api.py) for API usage and application |
      | ptrarchive | No | Yes | Please refer to [api.py](../config/api.py) for API usage and application |
      | riddler | No | Yes | Please refer to [api.py](../config/api.py) for API usage and application |
      | robtex | No | No | |
      | securitytrails_api | No | Yes | Please refer to [api.py](../config/api.py) for API usage and application |
      | sitedossier | No | No | |
      | threatcrowd | No | No | |
      | ximcx | No | No | |
 5. Use DNS query to collect subdomains (currently there is 1 module: collect subdomains `srv` by enumerating common SRV records and querying, this module needs to be added and improved)

       | Module name | Do you need a proxy | Do you need an API | Other instructions |
       | -------- | ------------ | ----------- | --------------- -------------- |
       | srv | No | No | Enumerate common SRV records of domain names to find subdomains |
   6. Use threat platform data collection subdomains (currently there are 6 modules: `riskiq_api`, `threatbook_api`, `threatminer`, `virustotal`, `virustotal_api` This module has yet to be added and improved)
      | Module name | Do you need a proxy | Do you need an API | Other instructions |
       | -------------- | ------------ | ----------- | --------- ---------------------------------------- |
       | alienvault | No | No | |
       | riskiq_api | No | Yes | Please refer to [api.py](../config/api.py) for API usage and application |
       | threatbook_api | No | Yes | See [api.py](../config/api.py) for API usage and application |
       | threatminer | No | No | |
       | virustotal | No | No | |
       | virustotal_api | No | Yes | Please refer to [api.py](../config/api.py) for API usage and application |
  7. Use search engines to discover subdomains (currently there are 16 modules: `ask`, `bing_api`, `fofa_api`, `shodan_api`, `yahoo`, `baidu`, `duckduckgo`, `github`, `google` , `so`, `yandex`, `bing`, `exalead`, `google_api`, `sogou`, `zoomeye_api`)

     Except for special search engines, general search engines support automatic exclusion search, full search, and recursive search.

     | Module | Do you need a proxy | Do you need an API | Other instructions |
     | ----------- | ---------------------- | -----------| - -------------------------------------------------- ------- |
     | ask | yes | no | |
     | baidu | No | No | |
     | bing | No | No | |
     | bing_api | No | Yes | Please refer to [api.py](../config/api.py) for API usage and application |
     | duckduckgo | yes | no | |
     | exalead | No, it is better to use a foreign agent. | No | |
     | fofa_api | No | Yes | Please refer to [api.py](../config/api.py) for API usage and application |
     | gitee | No | No | |
     | github | No | No | Set Github email name and password in [api.py](../config/api.py). |
     | google | yes | no | |
     | google_api | Yes | Yes | Please refer to [api.py](../config/api.py) for API usage and application |
     | shodan_api | No, it is better to use a foreign agent. | Yes | Please refer to [api.py](../config/api.py) for API usage and application |
     | so | No | No | |
     | sogou | No | No | |
     | yahoo | yes | no | |
     | yandex | yes | no | |
     | zoomeye_api | No | Yes | Please refer to [api.py](../config/api.py) for API usage and application               |
