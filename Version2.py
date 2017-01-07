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




#THIS IS WHERE I COMBINED THE 2 different versions for now


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




with open('exittesting.csv',encoding='latin-1') as csv123file:
    with open('exit2.csv', 'w', newline='') as open123file:
        webpage=open('index.html','w')
        acphtml=open('acp.html', 'w')
        humhtml=open('hum.html', 'w')
        ssbshtml=open('ssbs.html', 'w')
        cnwhtml=open('cnw.html', 'w')
        cwhtml=open('cw.html', 'w')
        wrapper = """ <tr>
        <td class="lalign"><a href= "%s">%s</a></td>
        <td>%s</td>
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
<ul>
    <li><a class="active" href="./index.html">All</a></li>
    <li><a href="./acp.html">ACP</a></li>
    <li><a href="./hum.html">Humanities and the Arts</a></li>
    <li><a href="./ssbs.html">Social/Behavioral</a></li>
    <li><a href="./cw.html">Western</a></li>
    <li><a href="./cnw.html">Non-Western</a></li>
</ul>
 <div id="wrapper">
  <h1>Grade Distribution Course Explorer</h1>

  <table id="keywords" cellspacing="0" cellpadding="0">
    <thead>
      <tr>
        <th><span>Class</span></th>
        <th><span>Class Title</span></th>
        <th><span>Total Students</span></th>
        <th><span>Credit Hours</span></th>
        <th><span>Percent A+/A</span></th>
        <th><span>Percent A+/A/A-</span></th>
      </tr>
    </thead>
    <tbody>""")

        acphtml.write("""<!doctype html>
        <html lang="en-US">
        <head>
          <meta charset="utf-8">
          <meta http-equiv="Content-Type" content="text/html">
          <title>ACP Classes Grade Distribution Explorer</title>
          <meta name="author" content="Jake Rocheleau">
          <link rel="shortcut icon" href="http://d15dxvojnvxp1x.cloudfront.net/assets/favicon.ico">
          <link rel="icon" href="http://d15dxvojnvxp1x.cloudfront.net/assets/favicon.ico">
          <link rel="stylesheet" type="text/css" media="all" href="css/styles.css">
          <script type="text/javascript" src="js/jquery-1.10.2.min.js"></script>
          <script type="text/javascript" src="js/jquery.tablesorter.min.js"></script>
        </head>

        <body>
<ul>
    <li><a class="active" href="./index.html">All</a></li>
    <li><a href="./acp.html">ACP</a></li>
    <li><a href="./hum.html">Humanities and the Arts</a></li>
    <li><a href="./ssbs.html">Social/Behavioral</a></li>
    <li><a href="./cw.html">Western</a></li>
    <li><a href="./cnw.html">Non-Western</a></li>
</ul>
         <div id="wrapper">
          <h1>ACP Classes Grade Distribution Explorer</h1>

          <table id="keywords" cellspacing="0" cellpadding="0">
            <thead>
              <tr>
                <th><span>Class</span></th>
                <th><span>Class Title</span></th>
                <th><span>Total Students</span></th>
                <th><span>Credit Hours</span></th>
                <th><span>Percent A+/A</span></th>
                <th><span>Percent A+/A/A-</span></th>
              </tr>
            </thead>
            <tbody>""")

        humhtml.write("""<!doctype html>
        <html lang="en-US">
        <head>
          <meta charset="utf-8">
          <meta http-equiv="Content-Type" content="text/html">
          <title>Humanities and the Arts Grade Distribution Explorer</title>
          <meta name="author" content="Jake Rocheleau">
          <link rel="shortcut icon" href="http://d15dxvojnvxp1x.cloudfront.net/assets/favicon.ico">
          <link rel="icon" href="http://d15dxvojnvxp1x.cloudfront.net/assets/favicon.ico">
          <link rel="stylesheet" type="text/css" media="all" href="css/styles.css">
          <script type="text/javascript" src="js/jquery-1.10.2.min.js"></script>
          <script type="text/javascript" src="js/jquery.tablesorter.min.js"></script>
        </head>

        <body>
<ul>
    <li><a class="active" href="./index.html">All</a></li>
    <li><a href="./acp.html">ACP</a></li>
    <li><a href="./hum.html">Humanities and the Arts</a></li>
    <li><a href="./ssbs.html">Social/Behavioral</a></li>
    <li><a href="./cw.html">Western</a></li>
    <li><a href="./cnw.html">Non-Western</a></li>
</ul>
         <div id="wrapper">
          <h1>Humanities and the Arts Grade Distribution Explorer</h1>

          <table id="keywords" cellspacing="0" cellpadding="0">
            <thead>
              <tr>
                <th><span>Class</span></th>
                <th><span>Class Title</span></th>
                <th><span>Total Students</span></th>
                <th><span>Credit Hours</span></th>
                <th><span>Percent A+/A</span></th>
                <th><span>Percent A+/A/A-</span></th>
              </tr>
            </thead>
            <tbody>""")

        ssbshtml.write("""<!doctype html>
        <html lang="en-US">
        <head>
          <meta charset="utf-8">
          <meta http-equiv="Content-Type" content="text/html">
          <title>Social/Behavioral Classes Grade Distribution Course Explorer</title>
          <meta name="author" content="Jake Rocheleau">
          <link rel="shortcut icon" href="http://d15dxvojnvxp1x.cloudfront.net/assets/favicon.ico">
          <link rel="icon" href="http://d15dxvojnvxp1x.cloudfront.net/assets/favicon.ico">
          <link rel="stylesheet" type="text/css" media="all" href="css/styles.css">
          <script type="text/javascript" src="js/jquery-1.10.2.min.js"></script>
          <script type="text/javascript" src="js/jquery.tablesorter.min.js"></script>
        </head>

        <body>
<ul>
    <li><a class="active" href="./index.html">All</a></li>
    <li><a href="./acp.html">ACP</a></li>
    <li><a href="./hum.html">Humanities and the Arts</a></li>
    <li><a href="./ssbs.html">Social/Behavioral</a></li>
    <li><a href="./cw.html">Western</a></li>
    <li><a href="./cnw.html">Non-Western</a></li>
</ul>
         <div id="wrapper">
          <h1>Social/Behavioral Classes Grade Distribution Explorer</h1>

          <table id="keywords" cellspacing="0" cellpadding="0">
            <thead>
              <tr>
                <th><span>Class</span></th>
                <th><span>Class Title</span></th>
                <th><span>Total Students</span></th>
                <th><span>Credit Hours</span></th>
                <th><span>Percent A+/A</span></th>
                <th><span>Percent A+/A/A-</span></th>
              </tr>
            </thead>
            <tbody>""")

        cnwhtml.write("""<!doctype html>
        <html lang="en-US">
        <head>
          <meta charset="utf-8">
          <meta http-equiv="Content-Type" content="text/html">
          <title>Non-Western Distribution Course Explorer</title>
          <meta name="author" content="Jake Rocheleau">
          <link rel="shortcut icon" href="http://d15dxvojnvxp1x.cloudfront.net/assets/favicon.ico">
          <link rel="icon" href="http://d15dxvojnvxp1x.cloudfront.net/assets/favicon.ico">
          <link rel="stylesheet" type="text/css" media="all" href="css/styles.css">
          <script type="text/javascript" src="js/jquery-1.10.2.min.js"></script>
          <script type="text/javascript" src="js/jquery.tablesorter.min.js"></script>
        </head>

        <body>
<ul>
    <li><a class="active" href="./index.html">All</a></li>
    <li><a href="./acp.html">ACP</a></li>
    <li><a href="./hum.html">Humanities and the Arts</a></li>
    <li><a href="./ssbs.html">Social/Behavioral</a></li>
    <li><a href="./cw.html">Western</a></li>
    <li><a href="./cnw.html">Non-Western</a></li>
</ul>

         <div id="wrapper">
          <h1>Non-Western Distribution Course Explorer</h1>

          <table id="keywords" cellspacing="0" cellpadding="0">
            <thead>
              <tr>
                <th><span>Class</span></th>
                <th><span>Class Title</span></th>
                <th><span>Total Students</span></th>
                <th><span>Credit Hours</span></th>
                <th><span>Percent A+/A</span></th>
                <th><span>Percent A+/A/A-</span></th>
              </tr>
            </thead>
            <tbody>""")
        cwhtml.write("""<!doctype html>
        <html lang="en-US">
        <head>
          <meta charset="utf-8">
          <meta http-equiv="Content-Type" content="text/html">
          <title>Cultural Western Grade Distribution Course Explorer</title>
          <meta name="author" content="Jake Rocheleau">
          <link rel="shortcut icon" href="http://d15dxvojnvxp1x.cloudfront.net/assets/favicon.ico">
          <link rel="icon" href="http://d15dxvojnvxp1x.cloudfront.net/assets/favicon.ico">
          <link rel="stylesheet" type="text/css" media="all" href="css/styles.css">
          <script type="text/javascript" src="js/jquery-1.10.2.min.js"></script>
          <script type="text/javascript" src="js/jquery.tablesorter.min.js"></script>
        </head>

        <body>
<ul>
    <li><a class="active" href="./index.html">All</a></li>
    <li><a href="./acp.html">ACP</a></li>
    <li><a href="./hum.html">Humanities and the Arts</a></li>
    <li><a href="./ssbs.html">Social/Behavioral</a></li>
    <li><a href="./cw.html">Western</a></li>
    <li><a href="./cnw.html">Non-Western</a></li>
</ul>
         <div id="wrapper">
          <h1>Cultural Western Grade Distribution Course Explorer</h1>

          <table id="keywords" cellspacing="0" cellpadding="0">
            <thead>
              <tr>
                <th><span>Class</span></th>
                <th><span>Class Title</span></th>
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
        versusClassTitle= 'Intro Asian American Studies'
        versusAplus=0
        versusA=0
        versusAminus = 0
        versustotal4=0
        versustotalA=0
        versustotalkids=0
        semester = 'S'
        year = '2016'
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
                    courseLink = 'https://courses.illinois.edu/schedule/2017/spring/' + versusSubject + '/' + versusNumber
                    if semester[0]=='F':
                        actuallink = 'http://courses.illinois.edu/cisapp/explorer/schedule/'+year+'/fall/' + versusSubject + '/' + versusNumber + '.xml?mode=cascade'

                    if semester[0]=='S':
                        actuallink = 'http://courses.illinois.edu/cisapp/explorer/schedule/' + year + '/spring/' + versusSubject + '/' + versusNumber + '.xml?mode=cascade'

                    courseLink = 'https://courses.illinois.edu/schedule/2017/spring/' + versusSubject + '/' + versusNumber
                    print(versus)

                    credithoururl = urllib.request.urlopen(actuallink).read()
                    creditsoup = BeautifulSoup(credithoururl, "lxml")
                    letters = creditsoup.find_all('credithours')
                    letter = letters[0]
                    stringified = str(letter)
                    credithours = stringified[13]

                    writer.writerow({'Course Title': versus, 'Course Subject': versusSubject, 'A+': versusAplus, 'A': versusA,
                                     'Total 4.0': versustotal4, 'Total A': versustotalA, 'Total Kids': versustotalkids,
                                     'Percent 4.0': versuspercent4, 'Percent A': versuspercentA, 'ACP': isACP, 'HUM': isHUM,
                                     'SSBS': isSSBS, 'CW': isCW, 'CNW': isCNW, 'Credit Hours': credithours})
                    webout= wrapper % (courseLink,versus, versusClassTitle, versustotalkids, credithours, versuspercent4, versuspercentA)
                    if isACP=='Yes':
                        acphtml.write(webout)
                    if isHUM=='Yes':
                        humhtml.write(webout)
                    if isSSBS=='Yes':
                        ssbshtml.write(webout)
                    if isCNW=='Yes':
                        cnwhtml.write(webout)
                    if isCW=='Yes':
                        cwhtml.write(webout)
                    webpage.write(webout)
                    webpage.write("\n")
                    versus = checking_course
                    versusSubject = row['Course Subject']
                    versusNumber = row['Course Number']
                    versusClassTitle = row['Course Title']
                    versusAplus = int(row['A+'])
                    versusA = int(row['A'])
                    versusAminus = int(row['A-'])
                    versustotal4 = int(row['A+'])+int(row['A'])
                    versustotalA = int(row['A+'])+int(row['A'])+int(row['A-'])
                    versustotalkids = int(row['A+'])+int(row['A'])+int(row['A-'])+int(row['B+'])+int(row['B'])+int(row['B-'])+int(row['C+'])+int(row['C'])+int(row['C-'])+int(row['D+'])+int(row['D'])+int(row['D-'])+int(row['F'])
                    semester=row['Semester']
                    year = '20' + semester[2] + semester[3]
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

acphtml.write(
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

humhtml.write(
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

ssbshtml.write(
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

cnwhtml.write(
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

cwhtml.write(
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
