import requests

url = "http://ws.clarin-pl.eu/nlprest2/base/process"
payload = "{\n    \"text\": \"Ala ma kota i wszyscy jej zazdroszczą. Jej kot jest leniwy, ale nikt o tym nie wie.\",\n    \"lpmn\": \"morphoDita\",\n    \"user\": \"xxx@yyy.com\"\n}"
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data = payload)

print(response.text.encode('utf8'))

payload = "{\n    \"text\": \"Ala ma kota i wszyscy jej zazdroszczą. Jej kot jest leniwy, ale nikt o tym nie wie.\",\n    \"lpmn\": \"wcrft2\",\n    \"user\": \"xxx@yyy.com\"\n}"

response = requests.request("POST", url, headers=headers, data = payload)

print(response.text.encode('utf8'))
