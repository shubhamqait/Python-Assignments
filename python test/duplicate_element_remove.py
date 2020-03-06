import re
import requests
import json
username = 'shubhamgupta'
password = 'qainfotech'
url = "http://10.0.10.198:8000/api/v1/challenges/5/?format=json"
response = requests.get(url, auth = (username,password))    
show = response.json()
data1 = show.get('sample_input')
data2 = data1.get('list')
l1 = []
for x in data2:
    if x not in l1: l1.append(x)
print(l1)
data3 = {
    'candidate':3,
    'challenge':5
}
url1 = "http://10.0.10.198:8000/api/v1/testsessions/"
check = requests.post(url,data = data3,auth = (username,password))

print(check.content)
sample_output = {'list':l1}
