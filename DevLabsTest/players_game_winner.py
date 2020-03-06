import re
import requests
import json
import ast 
username = 'shubham2'
password = 'Shubham#123'

url = "https://code-riddler.herokuapp.com/api/v1/challenges/get_challenge/"
response = requests.get(url, auth = (username,password)) 
show = response.json()
# print(show)
data1 = show.get('test_input')
data2 = data1.get('list')
data3 = data2
data4 = ast.literal_eval(data3)  
data5 = data4.get('player1')

pot = 1000
l1 = []
for x in data5:
    if x[0] == 'SP':
        y = 100
    elif x[0] == 'CL':
        y = 50
    elif x[0] == 'HT':
        y = -100
    elif x[0] == 'DD':
        y = -50

    if x[1] == 'SP':
        z = 100
    elif x[1] == 'CL':
        z = 50
    elif x[1] == 'HT':
        z = -100
    elif x[1] == 'DD':
        z = -50
    s = y + z
    l1.append(s) 
total1 = 0
for x in range(0,len(l1)):
    total1 = total1 + l1[x]
total1 = total1 + pot

data6 = data4.get('player2')
l2 = []
for x in data6:
    if x[0] == 'SP':
        y = 100
    elif x[0] == 'CL':
        y = 50
    elif x[0] == 'HT':
        y = -100
    elif x[0] == 'DD':
        y = -50

    if x[1] == 'SP':
        z = 100
    elif x[1] == 'CL':
        z = 50
    elif x[1] == 'HT':
        z = -100
    elif x[1] == 'DD':
        z = -50
    s = y + z
    l2.append(s) 
total2 = 0
for x in range(0,len(l2)):
    total2 = total2 + l2[x]
total2 = total2 + pot


if total1 > total2:
    winner = 'player1'    
else:
    winner = 'player2'
    

data7 = {
    "test_session":19,
    "output": {"winner":winner},
    "challenge": 7
}
headers={'Content-type':'application/json', 'Accept':'application/json'}
url1 = "https://code-riddler.herokuapp.com/api/v1/testsessionchallenges/output/"
check = requests.post(url1,data = json.dumps(data7),auth = (username,password),headers=headers)

print(check.content)
