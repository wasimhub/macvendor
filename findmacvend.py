#!/usr/bin/python

import json
import requests

newdic={}
uio=input("Enter mac address: ")
ui=uio.split(":")


URL='https://macaddress.io/database/macaddress.io-db.json'
r=requests.get(URL)

with open('dumpfile', 'wb') as f:
  f.write(r.content)

with open('dumpfile', 'r') as f:
  lines=f.readlines()
  for line in lines:
    found = True
    newdic=json.loads(line)
    l = newdic['oui'].split(":") 
    for i in range(len(l)):
      if l[i].upper() != ui[i].upper(): 
        found = False
        break

    if found != False:
      print("OUI vendor for mac {} is {}".format(uio, newdic['companyName']))
      break

