import csv
from bs4 import BeautifulSoup
import urllib.request

def k(a,b):
    def _k(item):
        return (item[a],item[b])
    return _k


classarray=[]
listoffiles=['30-F-15.csv','31-S-16.csv','28-S-15.csv']
for file in listoffiles:
    x=0
    with open(file, encoding='latin-1') as csv123file:
        reader = csv.DictReader(csv123file)
        for row in reader:
            tobeappended=[]
            if x==0:
                x=x+1
            elif row['A+']!='N/A':
                topics=['Course Subject','Course Number', 'Course Title', 'A+','A','A-','B+','B','B-','C+','C','C-','D+','D','D-','F']
                for item in topics:
                    tobeappended.append(row[item])
                tobeappended.append(file[3:7])
                classarray.append(tobeappended)

classarray=sorted(classarray, key=k(0,1))

for item in classarray:
    print(item)


with open('exittesting.csv', 'w', encoding='latin-1', newline='') as open123file:
    fieldnames = ['Course Subject','Course Number', 'Course Title', 'A+','A','A-','B+','B','B-','C+','C','C-','D+','D','D-','F', 'Semester']
    writer = csv.DictWriter(open123file, fieldnames=fieldnames)
    writer.writeheader()
    for item in classarray:
        writer.writerow({'Course Subject': item[0], 'Course Number':item[1], 'Course Title':item[2], 'A+':item[3], 'A':item[4], 'A-':item[5],'B+':item[6],'B':item[7],'B-':item[8],'C+':item[9],'C':item[10],'C-':item[11],'D+':item[12],'D':item[13],'D-':item[14],'F':item[15], 'Semester':item[16]})