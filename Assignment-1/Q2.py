''' Q2) Write a Python program that accepts a comma-separated sequence of words as input
and prints the words in a comma-separated sequence after sorting them alphabetically.
Suppose the following input is supplied to the program:
>> orange,apple,mango,grapes
Then, the output should be:
>> apple,grapes,mango,orange'''


items = input("Enter fruit's name with comma seprator \n")
words = [fruit for fruit in items.split(",")]  #fruit's in items is seprated by comma 
print(",".join(sorted(words)))
