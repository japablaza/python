#!/usr/bin/python3
import json
import requests

#Getting the data from Media player
url = 'https://<url>/device/<hostname>/system/dev/<status>'
username = 'usuario'
password = 'contrasenia'
sbsinfo = requests.get(url, auth=(username, password)).content
#print(sbsinfo)
#print('The data at this point should be bytes')
#print(type(sbsinfo))
b = sbsinfo.decode('utf-8').replace("'", '"')

print('The data at this point should be string')
#print(b)
print(type(b))

#Taking JSON string and convert it to a dictionary
datastore = json.loads(b)
print('Datastore type')
print(type(datastore))
print(datastore["identity"])
c = datastore["identity"]
print(type(c))
print(c["IP"])

direc = c["IP"]

if c != 22:
	print("Hola mundo")
