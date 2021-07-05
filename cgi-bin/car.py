#! /usr/bin/python3

print("content-type: text/html")
print()


import cgi
import subprocess as sp
import requests
import xmltodict
import json

db = cgi.FieldStorage()
ch=db.getvalue("ch")
url =("http://www.regcheck.org.uk/api/reg.asmx/CheckIndia?RegistrationNumber={}&username=<username>" .format(ch))
url=url.replace(" ","%20")
r = requests.get(url)
n = xmltodict.parse(r.content)
k = json.dumps(n)
df = json.loads(k)
l=df["Vehicle"]["vehicleJson"]
p=json.loads(l)
output="Your car's details are:\n"+"Owner name: "+str(p['Owner'])+"\n"+"Car Company: "+str(p['CarMake']['CurrentTextValue'])+"\n"+"Car Model: "+str(p['CarModel']['CurrentTextValue'])+"\n"+"Fuel Type: "+str(p['FuelType']['CurrentTextValue'])+"\n"+"Registration Year: "+str(p['RegistrationYear'])+"\n"+"Insurance: "+str(p['Insurance'])+"\n"+"Vehicle ID: "+str(p['VechileIdentificationNumber'])+"\n"+"Engine No.: "+str(p['EngineNumber'])+"\n"+"Location RTO: "+str(p['Location'])
print(output)
