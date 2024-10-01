# VulnVault
## Just a pretty simple program I made to search for CVEs by Vulnerability or by Service and/or Service Version.
## Requires a VulDB API key that can be obtained for free at https://www.vuldb.com
### Arguments:
- --search [term] (search for vulnerabilities based on a keyword. I.E. XSS, etc)
- --service [keyword] (search based on the name of a service. I.E. OpenSSH)
- --version [Integer] ( used when searching by service and you want to narrow down to a specific version number I.E. 8.1)

### Example usage: 
- python vulnvault.py --search XSS (search for all XSS based CVES)
- python vulnvault.py --service OpenSSH --version 8.1 (search for CVEs related to OpenSSH 8.1)