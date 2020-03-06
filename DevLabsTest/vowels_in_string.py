import re
import requests
import json
username = 'shubham2'
password = 'Shubham#123'

url = "https://code-riddler.herokuapp.com/api/v1/challenges/get_challenge/"
response = requests.get(url, auth = (username,password)) 
show = response.json()
# print(show)
data1 = show.get('test_input')
data2 = data1.get('text')
a=0
e=0
i=0
o=0
u=0
for x in data2:
    if x == 'a' or x == 'A':
        a = a + 1
    elif x == 'e' or x == 'E':
        e = e + 1
    elif x == 'i' or x == 'I':
        i = i + 1
    elif x == 'o' or x == 'O':
        o = o + 1
    elif x == 'u' or x == 'U':
        u = u + 1
    else:
        pass
sample_output = {'a':a,'e':e,'i':i,'o':o,'u':u}
data3 = {
    "test_session":19,
    "output": sample_output,
    "challenge": 4
}

headers={'Content-type':'application/json', 'Accept':'application/json'}
url1 = "https://code-riddler.herokuapp.com/api/v1/testsessionchallenges/output/"
check = requests.post(url1,data = json.dumps(data3),auth = (username,password),headers=headers)

print(check.content)
