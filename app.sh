#!/bin/bash
python3 ./set.py

if ip route | grep default > /dev/null
then
  #PC/ROOT
  python3 ./lanpc.py
else
  #MOBILE/UNROOT
  python3 ./lanmobi.py
fi 

echo
echo
python3 ./timex.py