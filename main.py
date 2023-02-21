import json

print("--------[ DADOS DA CONEXÃO ]--------\n")

with open("log.json", encoding='utf-8') as newjs:
    d = json.load(newjs)


print("IP PÚBLICO.....: {}\nREGIÃO.........: {}/{}\nISP............: {}".format(d["query"],d["country"],d["regionName"],d["isp"]))


newjs.close()