#!/bin/bash

cor0='\033[0;31m' #vermelho
fcor0='\033[0m'   #vermelho
cor1='\033[0;32m' #verde
fcor1='\033[0m'   #verde

echo TESTANDO CONEXÃO
echo

#status=`cat log.txt | grep success`
#echo $status

if ping -c 3 8.8.8.8 > /dev/null
then
   echo -e ${cor1}CONECTADO A INTERNET${fcor1}
   curl -s http://ip-api.com/json > log.json
   echo
   python3 main.py
else
   echo -e ${cor0}ERRO DE CONEXÃO COM A INTERNET${fcor0}
   
fi

###### REDE LOCAL

if ip route | grep default > /dev/null
then
    python3 default.py
else
    echo -e ${cor0}SEM ROTA COM UM GATEWAY VÁLIDO${fcor0}
fi
