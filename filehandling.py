import os
import shutil
entries = os.listdir('/home/shubham/Desktop/Folder')
filescreate=int(input("Enter how many files you want to create"))
for i in range(filescreate):
    f=open(str(i)+".txt","w+")

for entry in entries:
    print(entry)
filedir=int(input("Enter how many files you want to move in group"))
d=int(filescreate/filedir)
if a%filedir==0:
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
for x in range(d):
    for i in range(filedir):
        if y<filescreate: 
            source="/home/shubham/Desktop/Folder"+"/"+str(e*x+i)+".txt"
            destination="/home/shubham/Desktop/Folder/"+str(x)
            shutil.move(source,destination)
            y=y+1