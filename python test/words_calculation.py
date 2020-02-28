import re
import requests
import json
username = 'shubhamgupta'
password = 'qainfotech'
url = "http://10.0.10.198:8000/api/v1/challenges/2/?format=json"
response = requests.get(url, auth = (username,password))    
show = response.json()
data1 = show.get('sample_input')
data2 = data1.get('text') 
res = len(re.findall(r'\w+', data2)) 
data3 = {
    'candidate':3,
    'challenge':2
}
url1 = "http://10.0.10.198:8000/api/v1/testsessions/"
check = requests.post(url,data = data3,auth = (username,password))

print(check.content)
#print ("The number of words in string are : " +  str(res))
