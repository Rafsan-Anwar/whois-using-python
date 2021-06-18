import whois
import dns.resolver

result = dns.resolver.resolve('example.com', 'A')
for ipval in result:
    print('IP', ipval.to_text())


result = dns.resolver.resolve('example.com', 'CNAME')
for cnameval in result:
    print('CNAME target address:', cnameval.to_text())


result = dns.resolver.resolve('mail.example.com', 'MX')
# print(result.exchange)
for exdata in result:
    print('MX Record:', exdata.to_text())

result = dns.resolver.resolve('example.com', 'SOA')
# print(result.exchange)
for exdata in result:
    print('SOA Record:', exdata.to_text())


