import info
import json


network = info.dat0
net4 = info.datIpv4
net6 = info.datIpv6

ip = net4["local"]
cidr = int(net4["prefixlen"])
print('\n')

octetos_str = ip.split('.')
bloco = [int(octeto) for octeto in octetos_str]

ibit = 32 - cidr
bit = format(ibit, '08b')

bits = ibit * '0'
zbits = cidr * '1'
btx = zbits + bits


octetos = [btx[i:i+8] for i in range(0, len(btx), 8)]
decimal_octetos = [int(octeto, 2) for octeto in octetos]
n = 2 ** (32 - cidr) - 2

print(ip)
print(decimal_octetos)
print(n)

print(info.out)
