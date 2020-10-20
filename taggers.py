import requests
import json
import xml.etree.ElementTree as ET

url = "http://ws.clarin-pl.eu/nlprest2/base/process"
payload = json.dumps({"text": open("data\\test\\Albania_138293.txt", "r",encoding="utf-8").read(),
           "lpmn": "morphoDita",
           "user": "xxx@yyy.com"})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data = payload)

xml = response.text.encode('utf8')
myfile = open("morphoDita.xml", "wb")
myfile.write(xml)


payload = json.dumps({"text": open("data\\test\\Albania_138293.txt", "r",encoding="utf-8").read(),
           "lpmn": "wcrft2",
           "user": "xxx@yyy.com"})
response = requests.request("POST", url, headers=headers, data = payload)

xml = response.text.encode('utf8')
myfile = open("wcrft2.xml", "wb")
myfile.write(xml)