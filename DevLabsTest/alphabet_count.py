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
count = 0
for x in data2:
    if x != ' ':
        if x != '.':
            if x != '\n':
                count = count+1

data3 = {
    "test_session":19,
    "output": {'count':count},
    "challenge": 1
}
headers={'Content-type':'application/json', 'Accept':'application/json'}
url1 = "https://code-riddler.herokuapp.com/api/v1/testsessionchallenges/output/"
check = requests.post(url1,data = json.dumps(data3),auth = (username,password),headers=headers)

print(check.content)
