import os
import shutil
directory=os.path.dirname(os.path.realpath(__file__))
files=[]
files = os.listdir(directory)
length_of_files = len(files)
print("Total No. of files"+str(length_of_files))
source = directory

filedir = int(input("Enter how many files you want to move in group"))
d= int(length_of_files/filedir)
if length_of_files%filedir == 0:
    pass
else:
    d = d+1
for j in range(d):
    os.chdir(directory)
    if os.path.isdir(str(j)):
        pass
    else:
        os.mkdir(str(j))
e = filedir
y = 0
for x in range(d):
    for i in range(filedir):
        if y<length_of_files:
            sourcedata=directory+'/'+files[e*x+i]
            destinationdata=directory+"/"+str(x)
            shutil.move(sourcedata,destinationdata)
            y=y+1
