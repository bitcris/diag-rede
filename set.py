import requests
import json
import subprocess

print("TESTANDO CONEXÃO")

def wan():
    print("[ REDE WAN ]")
    req = requests.get('http://ip-api.com/json')
    d = json.loads(req.text)
    print("IP PÚBLICO..:",d["query"])
    print("REGIÃO......:",d["city"]+"/"+d["regionName"])
    print("PAÍS........:",d["country"])
    print("ISP.........:",d["isp"])


url = 'https://8.8.8.8'
try:
    s0 = requests.get(url, timeout=5)
    print("CONECTADO A INTERNET - STATUS {}\n".format(s0.status_code))
    wan()

except requests.exceptions.ConnectionError as erro:
    print("SEM CONEXÃO")

except requests.exceptions.Timeout as erro:
    print('ERRO DE CONEXÃO\nTEMPO LIMITE EXCEDIDO')



