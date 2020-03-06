import re
import requests
import json
username = 'shubham2'
password = 'Shubham#123'

url = "https://code-riddler.herokuapp.com/api/v1/challenges/get_challenge/"
response = requests.get(url, auth = (username,password)) 
show = response.json()
print(show)
data1 = show.get('test_input')
data2 = data1.get('list')
res = data2.strip('][').split(', ') 
print(res)
l1 = []
l2 = []
for x in res:
    if x not in l1:
        l1.append(int(x))
for y in l1:
    if y not in l2:
        l2.append(y)
print(l2)

data3 = {
    "test_session":19,
    "output": {'list':l2},
    "challenge": 5
}
headers={'Content-type':'application/json', 'Accept':'application/json'}
url1 = "https://code-riddler.herokuapp.com/api/v1/testsessionchallenges/output/"
check = requests.post(url1,data = json.dumps(data3),auth = (username,password),headers=headers)

print(check.content)
sample_output = {'list':l2}
