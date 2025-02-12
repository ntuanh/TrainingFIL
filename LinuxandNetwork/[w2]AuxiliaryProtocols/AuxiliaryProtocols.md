## Auxiliary Protocols .

### DNS - Domain Name System    
* A system translates human-readable domain name into IP address ( ex : example.com ---> 142.250.100.1 )
* How does work ? 
    * **User Request** : website URL ---> computer find it's IP address 
    * **Recursive Resolver** : find URL in cache ( faster )
    * **Root Name Server** : If the resolver does not have the answer , it ask a root name server , which directs it to a TLD(Top-Level Domain)
    (like `.com` or `.edu`)
    * **TLD** : directs the resolver to the authoritative name server for the requested domain.
    * **Authoritative** : This server provides the correct IP address .
    * Finally , Website loads .
    * TTL : Time To Line .
    * DNSSEC : DNS Security Extensions .
    * TLD : Top-Level Domain.
### NAT 

### DHCP 

### HTTP 

### FTP - File Transfer Protocol 