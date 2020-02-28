import re
import requests
import json
username = 'shubhamgupta'
password = 'qainfotech'
url = "http://10.0.10.198:8000/api/v1/challenges/4/?format=json"
response = requests.get(url, auth = (username,password))    
show = response.json()
data1 = show.get('sample_input')
data2 = data1.get('text')
count = 0
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
    'candidate':3,
    'challenge':4
}
url1 = "http://10.0.10.198:8000/api/v1/testsessions/"
check = requests.post(url,data = data3,auth = (username,password))

print(check.content)
#print (sample_output)
