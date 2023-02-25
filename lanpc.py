import subprocess
import json

protocolo = 'IPV4'

subprocess.run('ip -j route | grep default > gateway.json', shell=True)
with open("gateway.json", "r") as gjs:
    data0 = json.load(gjs)
    d0 = data0[0]
gjs.close()


subprocess.run('ip -j addr show dev {} > ip.json ; ip -j route show dev {} > gateway.json'.format(d0["dev"],d0["dev"]), shell=True)
with open("ip.json", "r") as ipjs:
    data1 = json.load(ipjs)
    d1 = data1[0]
    d1f = d1["addr_info"]
    size = len(d1f)
    f0 = d1f[0]
    if size > 0:
        protocolo = "IPV4/IPV6"
        f1 = d1f[1]
ipjs.close()


with open("gateway.json", "r") as redejs:
    data2 = json.load(redejs)
    d2 = data2[1]
redejs.close()


print("\n[ REDE LAN - {} ]".format(protocolo))
print("IP LOCAL....:",f0["local"])
print("GATEWAY.....:",d0["gateway"])
print("REDE........:",d2["dst"])
print("BROADCAST...:",f0["broadcast"])
if size > 0:
    print("IPv6:.......:",f1["local"])
print("INTERFACE...:",d0["dev"]) 
