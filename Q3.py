'''Q3) Write a Python program that accepts a sentence and calculates the number of letters
and digits.
Suppose the following input is supplied to the program:
>> hello world! 123
Then, the output should be:
>> LETTERS 10
DIGITS 3'''


string=input("Enter the word with digits\n")  #this take input as a string
d=l=0
for x in string:
  if x.isdigit():      #indigit function is used for identify the digits
    d=d+1
  elif c.isalpha():    #inalpha function is used fot identify the alphabet's
    l=l+1
  else:
    pass
print("Letter ",l)
print("Digit ",d)
