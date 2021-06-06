# Update log
All noteworthy changes to Garuda will be recorded in this file.

Garuda's update log format is based on [Keep a Changelog](https://keepachangelog.com/zh-CN/1.0.0/).

Garuda complies with [Semantic Version Format](https://semver.org/).

# Unreleased

# Released
## [0.4.3](https://github.com/shmilylty/oneforall/releases/tag/v0.4.3) - 2021-05-30
- Fixed known issues
- Updated documentation

## [0.4.2](https://github.com/shmilylty/oneforall/releases/tag/v0.4.2) - 2021-05-30
- Added the data table initialization process and fixed the problem in #163.

## [0.4.1](https://github.com/shmilylty/oneforall/releases/tag/v0.4.1) - 2021-05-30
- Fixed the problem of database error in the main domain (such as 58.com) beginning with a number

## [0.4.0](https://github.com/shmilylty/oneforall/releases/tag/v0.4.0) - 2021-05-30
-Refactored the subdomain request module to solve the problem of excessive memory usage
-Added a new subdomain replacement module, which can discover more new subdomains from existing subdomains
-Added data enrichment module to enrich more useful information
-Added the finder module, which can collect subdomains from the response body, JS and jump history
-Refactored pan-analytic detection, making pan-analytic detection more accurate
-Realized configuration plug-in design
-Implemented version update check, operating environment check, and network environment check
-Optimized the subdomain blasting module
-Optimized pan-analysis processing
-Optimized the subdomain dictionary
-Deleted and optimized some collection modules
-Fixed some feedback bugs
-Updated documentation

## [0.3.0](https://github.com/shmilylty/oneforall/releases/tag/v0.3.0) - 2021-05-31
-Refactored the project directory structure
-Modified the output display in English
-Optimized pan-analysis processing
-Optimized some collection modules
-Added silent level log output
-Added a dictionary of super-large blasting compressed packages
-Added a module for traversing DNS domains using NSEC records
-Added sublist3r interface query module
-Fixed some feedback bugs
-Updated documentation

## [0.2.0](https://github.com/shmilylty/oneforall/releases/tag/v0.2.0) - 2021-06-01
-Refactored the subdomain blasting and parsing module and switched to massdns. Generally, it can reach 10000pps, which is very fast
-Optimize pan-analysis processing
-Optimize some subdomain collection modules
-Added blasting dictionary
-Added github_api and rapiddns collection modules
-Fixed some bugs
-Updated documentation

## [0.1.0](https://github.com/shmilylty/oneforall/releases/tag/v0.1.0) - 2021-06-02
-Refactored Garuda entrance
-Add 1 new subdomain collection module
-Added two result fields: query type type and subdomain level level
-Adjust the project structure
-Optimize individual collection modules
-Optimize subdomain blasting dictionary
-Optimized response body decoding processing
-Update documentation
-Fix known bugs

## [0.0.9](https://github.com/shmilylty/oneforall/releases/tag/v0.0.9) - 2021-05-30
-Refactored the subdomain analysis module
-Add 4 new subdomain collection modules
-Added Docker deployment
-Optimize configuration parameters and collection modules
-Optimize subdomain blasting dictionary and default parameters
-Optimized response body decoding processing
-Update documentation
-Fix known bugs

## [0.0.8](https://github.com/shmilylty/oneforall/releases/tag/v0.0.8) - 2021-05-30
-Add new subdomain monitoring function
-Optimize subdomain blasting dictionary and default parameters
-Fix the port duplication problem
-Remove aiodns dependency

## [0.0.7](https://github.com/shmilylty/oneforall/releases/tag/v0.0.7) - 2021-05-22
-Fix some known issues
-Add Baidu cloud observation interface
-Add English Readme document
-Update related documents
-Optimize title acquisition
-Update dependencies

## [0.0.6](https://github.com/shmilylty/oneforall/releases/tag/v0.0.6) - 2021-05-30
-Fix some known issues
-Add PassiveDNS query and Github subdomain search module
-Optimize FoFa and BufferOver collection modules
-Update related documents
-Update dependencies
## [0.0.5](https://github.com/shmilylty/oneforall/releases/tag/v0.0.5) - 2021-06-02
-Fix some known bugs
-Optimize the collection interface of each subdomain and add a new subdomain collection interface
-Add subdomain DNS resolution and subdomain HTTP detection progress bar
-Add subdomain takeover risk check module and its instructions
-Update Garuda dependency

## [0.0.4](https://github.com/shmilylty/oneforall/releases/tag/v0.0.4) - 2021-05-11
### Repair
-Fix some known bugs

## [0.0.3](https://github.com/shmilylty/oneforall/releases/tag/v0.0.3) - 2021-05-08
### Modify
-Code PEP8 formatting
### Modify
-Modify some known bugs

## [0.0.2](https://github.com/shmilylty/oneforall/releases/tag/v0.0.2) - 2021-05-04
### New
-Added related documents
### Modify
-Modify the log output format and information
### Repair
-Upgrade the fire library version to solve the problem of running error
### Remove
-Remove brotlipy dependency


## [0.0.1](https://github.com/shmilylty/oneforall/releases/tag/v0.0.1) - 2021-05-02
### New
-Added the function of checking crossdomain.xml to collect subdomains
-Added the function of checking domain name certificate collection subdomain
-Added the function of checking content security policy header to collect subdomains
-Added domain transfer function
-Added subdomain collection function (search engine, DNS data set, certificate transparency, online crawler file)
-Added subdomain blasting function
-Added database export function