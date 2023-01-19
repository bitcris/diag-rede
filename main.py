import dns.resolver
import requests
import json
import subprocess


dns_resolver = dns.resolver.Resolver()
dns = dns_resolver.nameservers[0]



api = 'http://ip-api.com/json/'
apiDns = api+dns

reqDns = requests.get(apiDns)
reqIp = requests.get(api)
dataDns = json.loads(reqDns.text)
dataIp = json.loads(reqIp.text)

result = subprocess.run("ip route> log.txt", shell=True)
f = open("log.txt", "r")
dat = f.read()
rx = dat.split()
retorno = len(rx)

print("\n\n-------- DADOS DA REDE -------\n")
print('IP PÚBLICO: {}'.format(dataIp["query"]))
print('PROVEDOR: {}'.format(dataIp["isp"]))
print('PAÍS: {}\nREGIÃO: {}\n\n'.format(dataIp["country"], dataIp["regionName"]))

print("SERVIDOR DNS")
print('IP: {}\n\n'.format(dns))
print('SERVIDOR: {}\n\n'.format(dataDns["isp"]))

print("REDE LOCAL")
print(rx)
