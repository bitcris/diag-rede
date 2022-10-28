import requests
import json
import subprocess

url = 'http://ip-api.com/json'
p1 = requests.get(url)
data = json.loads(p1._content)
print("\nINFORMAÇÃO DA CONEXÃO\nDEV: Cristiano Ferreira\n\n")
print('IP PÚBLICO..: {}\nPAÍS........: {}\nREGIÃO......: {}\nPROVEDOR....: {}\n'.format(data["query"], data["country"], data["regionName"], data["isp"]))

result = subprocess.run("ip route> log.txt", shell=True)

def default():
  print("\nIP PRIVADO..: {}".format(rx[13]))
  print("REDE LOCAL..: {}".format(rx[5]))
  print("INTERFACE...: {}".format(rx[4]),"\n")

def mobile():
  print("\nIP PRIVADO..: {}".format(rx[8]))
  print("REDE LOCAL..: {}".format(rx[0]))
  print("INTERFACE...: {}".format(rx[2]),"\n")

f = open("log.txt", "r")
dat = f.read()
rx = dat.split()
retorno = len(rx)

if retorno > 9:
  default()
else:
  mobile()
