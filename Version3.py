import csv
from bs4 import BeautifulSoup
import urllib.request


def k(a,b,c):
    def _k(item):
        return (item[a],item[b],item[c])
    return _k


classarray=[]
listoffiles=['28-S-15.csv','30-F-15.csv','31-S-16.csv','33-F-16.csv']
y=0
for file in listoffiles:
    x=0
    with open(file, encoding='latin-1') as csv123file:
        reader = csv.DictReader(csv123file)
        for row in reader:
            y=y+1
            tobeappended=[]
            if x==0:
                x=x+1
            elif row['A+']!='N/A':
                topics=['Course Subject','Course Number', 'Course Title', 'A+','A','A-','B+','B','B-','C+','C','C-','D+','D','D-','F']
                for item in topics:
                    tobeappended.append(row[item])
                tobeappended.append(file[3:7])
                classarray.append(tobeappended)

classarray=sorted(classarray, key=k(0,1,2))
###CLASSARRAY IS NOW A SORTED LIST OF CLASSES

itemx = ['','','',0,0,0,0,0,0,0,0,0,0,0,0,0,'']
newarray=[]
for course,courseplus1 in zip(classarray,classarray[1:]):
    if (course[0]==courseplus1[0] and course[1]==courseplus1[1] and course[2]==courseplus1[2]):
        itemx[0]=course[0]
        itemx[1]=course[1]
        itemx[2]=course[2]
        for number in range(3,16):
            itemx[number]=itemx[number]+(int(course[number])+int(courseplus1[number]))
        itemx[16]=course[16]
    else:
        newarray.append(itemx)
        itemx = ['', '', '', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '']
        itemx[0]=courseplus1[0]
        itemx[1]=courseplus1[1]
        itemx[2]=courseplus1[2]
        for number in range(3,16):
            itemx[number]=int(courseplus1[number])
        itemx[16] = courseplus1[16]

#For Debugging Purposes
for item in newarray:
    print(item)

genedCodes=['ACP','HUM','SBS','CW','CNW']
classesListedByGened=[]

for code in genedCodes:
    urlWrapper="""https://courses.illinois.edu/search?year=2017&term=fall&keyword=&keywordType=qs&instructor=&collegeCode=&subjectCode=&creditHour=&degreeAtt=&courseLevel=&genedCode1=%s&genedCode2=&genedCode3=&partOfTerm=&_online=on&_open=on&_evenings=on"""
    url=urlWrapper % (code)
    openUrl = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(openUrl,"lxml")
    letters = soup.find_all('a')
    courses=[]
    x=0
    for letter in letters:
        link = letter.get('href')
        if len(link)>10:
            if link[8]=='s':
                x=x+1
                blank, search123, schedule, year, semester, department, classnumber = link.split("/")
                classnumber, junk = classnumber.split('?')
                actualClass = department + classnumber
                courses.append(actualClass)
    classesListedByGened.append(courses)
    print(x)

for gened in classesListedByGened:
    print(gened)

indexhtml = open('index.html', 'w')
acphtml = open('acp.html', 'w')
humhtml = open('hum.html', 'w')
ssbshtml = open('ssbs.html', 'w')
cnwhtml = open('cnw.html', 'w')
cwhtml = open('cw.html', 'w')
indextraits=['Grade Distribution Course Explorer','Grade Distribution Course Explorer']
acptraits=['ACP Classes Grade Distribution Explorer','ACP Classes Grade Distribution Explorer']
humtraits=['Humanities and the Arts Grade Distribution Explorer','Humanities and the Arts  Distribution Explorer']
cwtraits=['Cultural Western Grade Distribution Course Explorer','Cultural Western Distribution Course Explorer']
cnwtraits=['Non-Western Distribution Course Explorer','Non-Western Distribution Course Explorer']
ssbstraits=['Social/Behavioral Classes Grade Distribution Course Explorer','Social/Behavioral Distribution Explorer']
listoftraits=[indextraits,acptraits,humtraits,ssbstraits,cwtraits,cnwtraits]
listofwebpages=[indexhtml,acphtml,humhtml,ssbshtml,cwhtml,cnwhtml]

htmlstarter="""<!doctype html>
<html lang="en-US">
<head>
  <meta charset="utf-8">
  <meta http-equiv="Content-Type" content="text/html">
  <title>%s</title>
  <meta name="author" content="Neil Patel">
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
    <!-- <li id="instructions">Navigate to a GenEd, or click on a course for spots!</li> -->
</ul>
 <div id="wrapper">
  <h1>%s</h1>

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
    <tbody>"""

x=0
for page in listofwebpages:
    text=htmlstarter %(listoftraits[x][0],listoftraits[x][1])
    page.write(text)
    x=x+1
htmlwrapper = """ <tr>
        <td class="lalign"><a href= "%s">%s</a></td>
        <td>%s</td>
        <td>%d</td>
        <td>%s</td>
        <td>%f</td>
        <td>%f</td>
      </tr>"""

for course in newarray:
    whichcourse = course[0] + course[1]
    print(whichcourse)
    totalFour=course[3]+course[4]
    totalA=course[3]+course[4]+course[5]
    totalKids=course[3]+course[4]+course[5]+course[6]+course[7]+course[8]+course[9]+course[10]+course[11]+course[12]+course[13]+course[14]+course[15]
    percent4=totalFour/totalKids*100
    percentA=totalA/totalKids*100
    year = '20' + course[16][2] + course[16][3]
    if course[16][0] == 'F':
        actuallink = 'http://courses.illinois.edu/cisapp/explorer/schedule/' + year + '/fall/' + course[0] + '/' + \
                     course[1] + '.xml?mode=cascade'
    else:
        actuallink = 'http://courses.illinois.edu/cisapp/explorer/schedule/' + year + '/spring/' + course[0] + '/' + \
                     course[1] + '.xml?mode=cascade'
    courseLink = 'https://courses.illinois.edu/schedule/2017/fall/' + course[0] + '/' + course[1]
    credithoururl = urllib.request.urlopen(actuallink).read()
    creditsoup = BeautifulSoup(credithoururl, "lxml")
    letters = creditsoup.find_all('credithours')
    letter = letters[0]
    credithours = str(letter)
    print(credithours)
    junk,credithours,junk=credithours.split('>')
    credithours, junk = credithours.split('h',maxsplit=1)
    print(credithours)
    tableBlob = htmlwrapper % (courseLink, whichcourse,course[2], totalKids, credithours, percent4, percentA)
    indexhtml.write(tableBlob)
    #ACP
    x=0
    for page in listofwebpages[1:]:
        for item in classesListedByGened[x]:
            if whichcourse==item:
                page.write(tableBlob)
        x=x+1

for page in listofwebpages:
    page.write("""    </tbody>
      </table>
     </div>
    <script type="text/javascript">
    $(function(){
      $('#keywords').tablesorter();
    });
    </script>
    </body>
    </html>""")