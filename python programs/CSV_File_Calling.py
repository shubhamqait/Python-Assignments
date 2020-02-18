#Question:- How to read CSV File
import csv

reader = csv.DictReader(open('/home/qainfotech/Desktop/PythonPrograms/data.csv'))
for row in reader:
    print(row)