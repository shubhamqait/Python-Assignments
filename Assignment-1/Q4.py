'''Q4) Given the following two sets find the intersection and remove those elements from the
first set.
Given:
>> First Set {65, 42, 78, 83, 23, 57, 29}
>> Second Set {67, 73, 43, 48, 83, 57, 29}
Expected Outcome:
>> Intersection is {57, 83, 29}
>> First Set after removing common element {65, 42, 78, 23}'''


FirstSet  = {23, 42, 65, 57, 78, 83, 29}
SecondSet = {57, 83, 29, 67, 73, 43, 48}

intersection = FirstSet.intersection(SecondSet)   #this line is used for seprating common digits
print("Intersection is ", intersection)
for item in intersection:                          #this is for removing common digits in FirstSet
  FirstSet.remove(item)

print("First Set after removing common element ", FirstSet)
