'''Q8) Iterate a given list and Check if a given element already exists in a dictionary as a key’s
value if not delete it from the list.
Given:
rollNumber = [47, 64, 69, 37, 76, 83, 95, 97]
sampleDict ={'A':47, 'B':69, 'C':76, 'D':97}
Expected Outcome:
New List [47, 69, 76, 97]'''


rollNumber=[47,64,69,37,76,83,95,97]
sampleDict ={'A':47,'B':69,'C':76,'D':97}
thisList=[]
for value in sampleDict.values():
  if value not in thisList:
    thisList.append(value)

for roll in rollNumber:
  if roll not in thisList:
    rollNumber.remove(roll)
print("New List",rollNumber)
