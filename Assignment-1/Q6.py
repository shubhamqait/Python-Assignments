'''Q6) Remove duplicate from a list and create a tuple and find the min and max number.
Given:
sampleList = [87, 45, 41, 65, 94, 41, 99, 94]
Expected Outcome:
>> unique items [87, 45, 41, 65, 99]
tuple (87, 45, 41, 65, 99)
min: 41
max: 99'''


sampleList = [87, 45, 41, 65, 94, 41, 99, 94]
uniqueList=[]
for item in sampleList:
  if item not in uniqueList:
    uniqueList.append(item)
print("Unique Items ",uniqueList)
tupleitem=tuple(uniqueList)
print("tuple",tupleitem)
print("min",min(tupleitem))
print("max",max(tupleitem))
