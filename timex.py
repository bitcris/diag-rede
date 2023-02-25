import requests
import time

cont = ['E-UNIDOS', 'CHINA', 'ITÁLIA', 'BRASIL']
link = ['http://142.251.133.164', 'http://203.205.251.163', 'http://15.161.156.80', 'http://177.37.220.25']

print("TEMPO DE RESPOSTA POR REGIÃO")


siz = len(cont)
n = 0

while n < siz:
 tmi = time.time()
 png = requests.get(link[n])
 tmf = time.time()
 ms = tmf - tmi
 msf = "{:.2f} ms".format(ms)
 cof = "{} -".format(cont[n])
 print(cof,msf)
 n = n + 1
 