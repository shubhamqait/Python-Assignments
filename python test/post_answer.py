import re
import requests
import json
username = 'shubham2'
password = 'Shubham#123'
url = "http://10.0.10.198:8000/api/v1/challenges/3/?format=json"
response = requests.get(url, auth = (username,password))    
show = response.json()
data1 = show.get('sample_input')
data2 = data1.get('text')
count = 0
for x in data2:
    if x == '.':
        count = count + 1

data3 = {
    'candidate':3,
    'challenge':3
}
url1 = "http://10.0.10.198:8000/api/v1/testsessions/"
check = requests.post(url,data = data3,auth = (username,password))

print(check.content)
#print ("The number of sentences in string are : " +  str(count))