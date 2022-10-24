import requests
import json
import subprocess

url = 'http://ip-api.com/json'

p1 = requests.get(url)
data = json.loads(p1._content)
print("\nINFORMAÇÃO DA CONEXÃO - DEV: Cristiano Ferreira\n\n")
print('IP..........: {}\nPAÍS........: {}\nREGIÃO......: {}\nPROVEDOR....: {}\n'.format(data["query"], data["country"], data["city"], data["isp"]))

result = subprocess.run("ifconfig eth0 > log.txt", shell=True)

with open(r"log.txt", 'r') as fp:
    line_numbers = [1]
    lines = []
    for i, line in enumerate(fp):
        if i in line_numbers:
            lines.append(line.strip())
        elif i > 1:
            break
print('CONEXÃO LOCAL:\n'+lines[0]+'\n')
