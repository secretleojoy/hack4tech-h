Note: some of the following fields are only stored in the result database

### id

Significant role

### new

Whether the tag is a newly discovered subdomain

### alive

Whether it is alive or not, the judgment of non-survival includes: unable to resolve IP, network unreachable, 400, 5XX, etc.

### request

Record whether the HTTP request is successful or not, if it is empty, the IP cannot be resolved, 0 is the network is unreachable, and 1 is the successful request

### resolve

Record whether DNS resolution is successful

### url

Requested url link

### subdomain

Subdomain

### level

What level of subdomain

### cname

cname record

### ip

Resolved IP

### public

Is it a public IP

### cdn

Is the resolved IP CDN

### port

Requested network port

### status

HTTP response status code

### reason

Network connection status and details

###title

Site title

### banner

Website fingerprint information

### history
URL redirection history on request

### response
Response body text content

### times

The number of ip repeated occurrences in blasting

### ttl

TTL value returned by DNS resolution

### cidr

CIDR queried by ip2location library

### asn

ASN queried by ip2location library

### addr

The physical address queried by the ip2region library

### isp

The network service provider queried by the ip2region library

### resolver

DNS resolution server used

### module

Discover the modules used by this subdomain

### source

Discover the specific source of this subdomain

### elapse

Current module discovery time

### find

The number of subdomains discovered by the current module