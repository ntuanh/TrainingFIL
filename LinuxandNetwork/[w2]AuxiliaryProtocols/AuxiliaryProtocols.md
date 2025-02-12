## Auxiliary Protocols .

### DNS - Domain Name System    
* A system translates human-readable domain name into IP address ( ex : example.com &#8594; 142.250.100.1 )
* How does work ? 
    * **User Request** : website URL &#8594; computer find it's IP address 
    * **Recursive Resolver** : find URL in cache ( faster )
    * **Root Name Server** : If the resolver does not have the answer , it ask a root name server , which directs it to a TLD(Top-Level Domain)
    (like `.com` or `.edu`)
    * **TLD** : directs the resolver to the authoritative name server for the requested domain.
    * **Authoritative** : This server provides the correct IP address .
    * Finally , Website loads .
        * TTL : Time To Line .
        * DNSSEC : DNS Security Extensions .
        * TLD : Top-Level Domain.

        ![DNS](/Images/DNS.png)

### NAT - Network Address Translation 
##### SNAT - Static NAT 
* One public IP address is mapped to one private IP address.
* Example : `192.168.1.1` (private) &#8594; `100.0.0.1` (public)
    
    ![SNAT](/Images/SNAT.png)

##### DNAT - Dynamic NAT
* Dynamic NAT assigns private IPs to the public IPs dynamically from a pool of the public IP address .
* Example : `192.168.1.1` (private) &#8594; `100.0.0.1` (public ). If `192.168.1.1` disconnect &#8594; return IP address to the pool for reuse .

### DHCP 
*

### HTTP 

### FTP - File Transfer Protocol 