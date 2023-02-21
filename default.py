import json
import subprocess

print("\n----------[ REDE LOCAL ]----------\n")

subprocess.run("ip -j route | grep default > local.json", shell=True)

with open("local.json", encoding='utf-8') as newjs:
    dados = json.load(newjs)

dat = dados[0]
#print(dat)
iface = dat["dev"]
newjs.close()

#INTERFACE ESPECÍFICA

subprocess.run("ip -j route show dev {} | grep default > interface.json".format(iface), shell=True)


with open("interface.json", encoding='utf-8') as newjs2:
  dados2 = json.load(newjs2)

  dat2 = dados2[1]
#print(dat2)

print("IP LOCAL.......: {}\nGATEWAY........: {}\nREDE...........: {}\nINTERFACE......: {}".format(dat2["prefsrc"],dat["gateway"],dat2["dst"],dat["dev"]))
   