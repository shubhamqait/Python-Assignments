# ankitksr: THE SCRIPT DOES NOT RUN.

import os
import shutil
# ankitksr: Do not use hard-coded folder paths. Instead, use relative paths.
entries = os.listdir('/home/shubham/Desktop/Folder')
filescreate=int(input("Enter how many files you want to create"))
# ankitksr: Do not assume that the files in the folder would be named as per your preferred naming scheme. Assume random file names.
for i in range(filescreate):
    f=open(str(i)+".txt","w+")

for entry in entries:
    print(entry)   # ankitksr: What is the purpose of this print statement?
filedir=int(input("Enter how many files you want to move in group"))
d=int(filescreate/filedir)
if a%filedir==0:   # ankitksr: What is 'a' here?
    pass
else:
    d=d+1
for j in range(d):
    os.chdir("/home/shubham/Desktop/Folder")
    if os.path.isdir(str(j)):
        pass
    else:
        os.mkdir(str(j))
e=filedir
y=0
# ankitksr: Unable to understand the logic used below.
for x in range(d):
    for i in range(filedir):
        if y<filescreate: 
            source="/home/shubham/Desktop/Folder"+"/"+str(e*x+i)+".txt"
            destination="/home/shubham/Desktop/Folder/"+str(x)
            shutil.move(source,destination)
            y=y+1
