import csv
from bs4 import BeautifulSoup
import urllib.request

acpurl = urllib.request.urlopen('https://courses.illinois.edu/search?year=2017&term=spring&keyword=&keywordType=qs&instructor=&collegeCode=&subjectCode=&creditHour=&degreeAtt=&courseLevel=&genedCode1=ACP&genedCode2=&genedCode3=&partOfTerm=&_online=on&_open=on&_evenings=on').read()
acpsoup = BeautifulSoup(acpurl,"lxml")
letters = acpsoup.find_all('a')
links=[]
x=0
for letter in letters:
    links.append(letter.get('href'))
classes=[]
for link in links:
    if len(link)>10:
        if link[8]=='s':
            classes.append(link)
acpCourses=[]
for clas in classes:
    x=x+1
    blank, search123, schedule, year, semester, department, classnumber = clas.split("/")
    classnumber, junk = classnumber.split('?')
    actualClass = department + classnumber
    acpCourses.append(actualClass)
print(x)

humurl = urllib.request.urlopen('https://courses.illinois.edu/search?year=2017&term=spring&keyword=&keywordType=qs&instructor=&collegeCode=&subjectCode=&creditHour=&degreeAtt=&courseLevel=&genedCode1=HUM&genedCode2=&genedCode3=&partOfTerm=&_online=on&_open=on&_evenings=on').read()
humsoup = BeautifulSoup(humurl, "lxml")
humletters = humsoup.find_all('a')
humlinks=[]
z=0
for letter in humletters:
    humlinks.append(letter.get('href'))
humclasses=[]
for link in humlinks:
    if len(link)>10:
        if link[8]=='s':
            humclasses.append(link)
humCourses=[]
for clas in humclasses:
    z=z+1
    blank, search123, schedule, year, semester, department, classnumber = clas.split("/")
    humclassnumber, humjunk = classnumber.split('?')
    humactualClass = department + humclassnumber
    humCourses.append(humactualClass)
print(z)

ssbsurl = urllib.request.urlopen('https://courses.illinois.edu/search?year=2017&term=spring&keyword=&keywordType=qs&instructor=&collegeCode=&subjectCode=&creditHour=&degreeAtt=&courseLevel=&genedCode1=SBS&genedCode2=&genedCode3=&partOfTerm=&_online=on&_open=on&_evenings=on').read()
ssbssoup = BeautifulSoup(ssbsurl, "lxml")
ssbsletters = ssbssoup.find_all('a')
ssbslinks=[]
z=0
for letter in ssbsletters:
    ssbslinks.append(letter.get('href'))
ssbsclasses=[]
for link in ssbslinks:
    if len(link)>10:
        if link[8]=='s':
            ssbsclasses.append(link)
ssbsCourses=[]
for clas in ssbsclasses:
    z=z+1
    blank, search123, schedule, year, semester, department, classnumber = clas.split("/")
    ssbsclassnumber, ssbsjunk = classnumber.split('?')
    ssbsactualClass = department + ssbsclassnumber
    ssbsCourses.append(ssbsactualClass)
print(z)


#THIS NEXT PART IS CNW I WAS TOO LAZY TO CHANGE VARIABLES
ssbsurl = urllib.request.urlopen('https://courses.illinois.edu/search?year=2017&term=spring&keyword=&keywordType=qs&instructor=&collegeCode=&subjectCode=&creditHour=&degreeAtt=&courseLevel=&genedCode1=CNW&genedCode2=&genedCode3=&partOfTerm=&_online=on&_open=on&_evenings=on').read()
ssbssoup = BeautifulSoup(ssbsurl , "lxml")
ssbsletters = ssbssoup.find_all('a')
ssbslinks=[]
z=0
for letter in ssbsletters:
    ssbslinks.append(letter.get('href'))
ssbsclasses=[]
for link in ssbslinks:
    if len(link)>10:
        if link[8]=='s':
            ssbsclasses.append(link)
cnwCourses=[]
for clas in ssbsclasses:
    z=z+1
    blank, search123, schedule, year, semester, department, classnumber = clas.split("/")
    ssbsclassnumber, ssbsjunk = classnumber.split('?')
    ssbsactualClass = department + ssbsclassnumber
    cnwCourses.append(ssbsactualClass)
print(z)

#THIS NEXT PART IS Western I WAS TOO LAZY TO CHANGE VARIABLES
ssbsurl = urllib.request.urlopen('https://courses.illinois.edu/search?year=2017&term=spring&keyword=&keywordType=qs&instructor=&collegeCode=&subjectCode=&creditHour=&degreeAtt=&courseLevel=&genedCode1=CW&genedCode2=&genedCode3=&partOfTerm=&_online=on&_open=on&_evenings=on').read()
ssbssoup = BeautifulSoup(ssbsurl, "lxml")
ssbsletters = ssbssoup.find_all('a')
ssbslinks=[]
z=0
for letter in ssbsletters:
    ssbslinks.append(letter.get('href'))
ssbsclasses=[]
for link in ssbslinks:
    if len(link)>10:
        if link[8]=='s':
            ssbsclasses.append(link)
westernCourses=[]
for clas in ssbsclasses:
    z=z+1
    blank, search123, schedule, year, semester, department, classnumber = clas.split("/")
    ssbsclassnumber, ssbsjunk = classnumber.split('?')
    ssbsactualClass = department + ssbsclassnumber
    westernCourses.append(ssbsactualClass)
print(z)




with open('30-F-15.csv',encoding='UTF-16') as csv123file:
    with open('exit2.csv', 'w', newline='') as open123file:
        webpage=open('webpage.html','w')
        wrapper = """ <tr>
        <td class="lalign">%s</td>
        <td>%d</td>
        <td>%s</td>
        <td>%f</td>
        <td>%f</td>
      </tr>"""
        webpage.write("""<!doctype html>
<html lang="en-US">
<head>
  <meta charset="utf-8">
  <meta http-equiv="Content-Type" content="text/html">
  <title>Grade Distribution Course Explorer</title>
  <meta name="author" content="Jake Rocheleau">
  <link rel="shortcut icon" href="http://d15dxvojnvxp1x.cloudfront.net/assets/favicon.ico">
  <link rel="icon" href="http://d15dxvojnvxp1x.cloudfront.net/assets/favicon.ico">
  <link rel="stylesheet" type="text/css" media="all" href="css/styles.css">
  <script type="text/javascript" src="js/jquery-1.10.2.min.js"></script>
  <script type="text/javascript" src="js/jquery.tablesorter.min.js"></script>
</head>

<body>
 <div id="wrapper">
  <h1>Grade Distribution Course Explorer</h1>

  <table id="keywords" cellspacing="0" cellpadding="0">
    <thead>
      <tr>
        <th><span>Class</span></th>
        <th><span>Total Students</span></th>
        <th><span>Credit Hours</span></th>
        <th><span>Percent A+/A</span></th>
        <th><span>Percent A+/A/A-</span></th>
      </tr>
    </thead>
    <tbody>""")




        fieldnames = ['Course Title','Course Subject', 'A+', 'A', 'Total 4.0', 'Total A', 'Total Kids', 'Percent 4.0', 'Percent A', 'ACP', 'HUM', 'SSBS', 'CW', 'CNW', 'Credit Hours']
        writer = csv.DictWriter(open123file,fieldnames=fieldnames)
        writer.writeheader()

        reader = csv.DictReader(csv123file)
        versus = 'AAS100'
        versusSubject= 'AAS'
        versusNumber= '100'
        versusAplus=0
        versusA=0
        versusAminus = 0
        versustotal4=0
        versustotalA=0
        versustotalkids=0
        for row in reader:
            y=row['A+']
            if y!='N/A':
                checking_course = row['Course Subject']+row['Course Number']
                if checking_course==versus:
                    versusAplus = versusAplus+int(row['A+'])
                    versusA = versusA+int(row['A'])
                    versusAminus= versusAminus+int(row['A-'])
                    versustotal4 = versusAplus+versusA
                    versustotalA = versusAplus+versusA+versusAminus
                    versustotalkids = versustotalkids+int(row['A+'])+int(row['A'])+int(row['A-'])+int(row['B+'])+int(row['B'])+int(row['B-'])+int(row['C+'])+int(row['C'])+int(row['C-'])+int(row['D+'])+int(row['D'])+int(row['D-'])+int(row['F'])

                else:
                    isACP = 'NO'
                    isHUM = 'NO'
                    isSSBS = 'NO'
                    isCNW = 'NO'
                    isCW = 'NO'
                    for string in acpCourses:
                        if string == versus:
                            isACP = 'Yes'
                    for string in humCourses:
                        if string == versus:
                            isHUM = 'Yes'
                    for string in ssbsCourses:
                        if string == versus:
                            isSSBS = 'Yes'
                    for string in cnwCourses:
                        if string == versus:
                            isCNW = 'Yes'
                    for string in westernCourses:
                        if string == versus:
                            isCW = 'Yes'
                    versuspercent4 = versustotal4 / versustotalkids
                    versuspercentA = versustotalA / versustotalkids
                    actuallink = 'http://courses.illinois.edu/cisapp/explorer/schedule/2015/fall/' + versusSubject + '/' + versusNumber + '.xml?mode=cascade'
                    print(actuallink)

                    credithoururl = urllib.request.urlopen(actuallink).read()
                    creditsoup = BeautifulSoup(credithoururl, "lxml")
                    letters = creditsoup.find_all('credithours')
                    letter = letters[0]
                    stringified = str(letter)
                    credithours = stringified[13]
                    print(credithours)

                    writer.writerow({'Course Title': versus, 'Course Subject': versusSubject, 'A+': versusAplus, 'A': versusA,
                                     'Total 4.0': versustotal4, 'Total A': versustotalA, 'Total Kids': versustotalkids,
                                     'Percent 4.0': versuspercent4, 'Percent A': versuspercentA, 'ACP': isACP, 'HUM': isHUM,
                                     'SSBS': isSSBS, 'CW': isCW, 'CNW': isCNW, 'Credit Hours': credithours})
                    webout= wrapper % (versus, versustotalkids, credithours, versuspercent4, versuspercentA)
                    webpage.write(webout)
                    webpage.write("\n")
                    versus = checking_course
                    versusSubject = row['Course Subject']
                    versusNumber = row['Course Number']
                    versusAplus = int(row['A+'])
                    versusA = int(row['A'])
                    versusAminus = int(row['A-'])
                    versustotal4 = int(row['A+'])+int(row['A'])
                    versustotalA = int(row['A+'])+int(row['A'])+int(row['A-'])
                    versustotalkids = int(row['A+'])+int(row['A'])+int(row['A-'])+int(row['B+'])+int(row['B'])+int(row['B-'])+int(row['C+'])+int(row['C'])+int(row['C-'])+int(row['D+'])+int(row['D'])+int(row['D-'])+int(row['F'])

webpage.write(
    """    </tbody>
  </table>
 </div>
<script type="text/javascript">
$(function(){
  $('#keywords').tablesorter();
});
</script>
</body>
</html>"""
)


