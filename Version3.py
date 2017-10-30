import csv
import getTechElectives
from bs4 import BeautifulSoup
import urllib.request


def k(a,b,c):
    def _k(item):
        return (item[a],item[b],item[c])
    return _k


classarray=[]
listoffiles=['28-S-15.csv','30-F-15.csv','31-S-16.csv','33-F-16.csv','34-S-17.csv']
y=0

# this for loop is to combine all four of the csv files into one big array
for file in listoffiles:
    #I use x to skip the first line of the CSV file b/c it has headers/column names
    x=0
    with open(file, encoding='latin-1') as csv123file:
        reader = csv.DictReader(csv123file)
        for row in reader:
            y=y+1
            tobeappended=[]
            if x==0:
                x=x+1
            elif row['A+']!='N/A':
                # Identify the topics that you want to keep in your new array
                topics=['Course Subject','Course Number', 'Course Title', 'A+','A','A-','B+','B','B-','C+','C','C-','D+','D','D-','F']
                for item in topics:
                    tobeappended.append(row[item])
                #What I'm doing here is adding a column that keeps track of what semester that class data is from
                tobeappended.append(file[3:7])
                classarray.append(tobeappended)

# sort class array by Subject,Number,and Course title
classarray=sorted(classarray, key=k(0,1,2))

# the purpose of this next for loop is to combine row data if it is the exact same class taught different semesters or different sections
#An example is ECON102, which is taught every semester;I want the summed data in one row

current_class_data = ['','','',0,0,0,0,0,0,0,0,0,0,0,0,0,'']
summed_class_data=[]
for course,courseplus1 in zip(classarray,classarray[1:]):
    #Check if 'Course Subject','Course Number', 'Course Title', are the same between then current and current+1 row 
    if (course[0]==courseplus1[0] and course[1]==courseplus1[1] and course[2]==courseplus1[2]):
        current_class_data[0]=course[0]
        current_class_data[1]=course[1]
        current_class_data[2]=course[2]
        #if yes then you need to add the data together
        for number in range(3,16):
            current_class_data[number]=current_class_data[number]+(int(course[number])+int(courseplus1[number]))
        current_class_data[16]=course[16]
    # if no then add it to summed_class_data and create a new current_class_data to represent the next class
    else:
        summed_class_data.append(current_class_data)
        current_class_data = ['', '', '', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '']
        current_class_data[0]=courseplus1[0]
        current_class_data[1]=courseplus1[1]
        current_class_data[2]=courseplus1[2]
        for number in range(3,16):
            current_class_data[number]=int(courseplus1[number])
        current_class_data[16] = courseplus1[16]

#For Monitoring/Debugging Purposes
for item in summed_class_data:
    print(item)

genedCodes=['ACP','HUM','SBS','CW','CNW']
classesListedByGened=[]

#here What I'm doing is hitting the course page of each gen-ed type to scrape a list of classes that fulfill that requirement
for code in genedCodes:
    #urlWrapper="""https://courses.illinois.edu/search?year=2017&term=fall&keyword=&keywordType=qs&instructor=&collegeCode=&subjectCode=&creditHour=&degreeAtt=&courseLevel=&genedCode1=%s&genedCode2=&genedCode3=&partOfTerm=&_online=on&_open=on&_evenings=on"""
    urlWrapper="""https://courses.illinois.edu/gened/2018/spring/%s"""
    url=urlWrapper % (code)
    openUrl = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(openUrl,"html5lib")
    letters = soup.find_all('a')
    courses=[]
    #x is for debugging; its just to check to see how many of each kind of gen-ed codes I have
    x=0
    for letter in letters:
        link = letter.get('href')
        if len(link)>8:
            if link[0:15]=='/schedule/2018/':
                print(link)
                x=x+1
                blank, schedule, year, semester, department, classnumber = link.split("/")
                actualClass = department + classnumber
                courses.append(actualClass)
    classesListedByGened.append(courses)
    print(x)

classesListedByGened.append(getTechElectives.get_tech_elective_list())
#For Monitoring/Debugging Purposes
for gened in classesListedByGened:
    print(gened)

#open various html files for writing to them 
indexhtml = open('index.html', 'w')
acphtml = open('acp.html', 'w')
humhtml = open('hum.html', 'w')
ssbshtml = open('ssbs.html', 'w')
cnwhtml = open('cnw.html', 'w')
cwhtml = open('cw.html', 'w')
techhtml=open('tech.html','w')
# identify the title/headers of the pages 
indextraits=['Grade Distribution Course Explorer','Grade Distribution Course Explorer']
acptraits=['ACP Classes Grade Distribution Explorer','ACP Classes Grade Distribution Explorer']
humtraits=['Humanities and the Arts Grade Distribution Explorer','Humanities and the Arts  Distribution Explorer']
cwtraits=['Cultural Western Grade Distribution Course Explorer','Cultural Western Distribution Course Explorer']
cnwtraits=['Non-Western Distribution Course Explorer','Non-Western Distribution Course Explorer']
ssbstraits=['Social/Behavioral Classes Grade Distribution Course Explorer','Social/Behavioral Distribution Explorer']
techtraits=['ECE Tech Electives Grade Distribution Course Explorer','Tech Elective Distribution Explorer']

#put the webpages and their traits in a list for easy looping
listoftraits=[indextraits,acptraits,humtraits,ssbstraits,cwtraits,cnwtraits,techtraits]
listofwebpages=[indexhtml,acphtml,humhtml,ssbshtml,cwhtml,cnwhtml,techhtml]

#Wrapper to intialize each html page
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

#come back and modify this for a range so I dont have to deal with this ugly variable increment
x=0
for page in listofwebpages:
    text=htmlstarter %(listoftraits[x][0],listoftraits[x][1])
    page.write(text)
    x=x+1

#wrapper for a table row 
htmlwrapper = """ <tr>
        <td class="lalign"><a href= "%s">%s</a></td>
        <td>%s</td>
        <td>%d</td>
        <td>%s</td>
        <td>%f</td>
        <td>%f</td>
      </tr>"""
#The real magic here is to create the table rows
#What I'm doing for each row is figuring out the total kids, the kids that got a 4.0, and the kids that got any kind of A in the class
for course in summed_class_data:
    whichcourse = course[0] + course[1]
    print(whichcourse)
    totalFour=course[3]+course[4]
    totalA=course[3]+course[4]+course[5]
    totalKids=course[3]+course[4]+course[5]+course[6]+course[7]+course[8]+course[9]+course[10]+course[11]+course[12]+course[13]+course[14]+course[15]
    percent4=totalFour/totalKids*100
    percentA=totalA/totalKids*100
    #Identify what year this data is from 
    year = '20' + course[16][2] + course[16][3]
    #Create a link to the original course listing to scrape the credit hour data
    if course[16][0] == 'F':
        actuallink = 'http://courses.illinois.edu/cisapp/explorer/schedule/' + year + '/fall/' + course[0] + '/' + \
                     course[1] + '.xml?mode=cascade'
    else:
        actuallink = 'http://courses.illinois.edu/cisapp/explorer/schedule/' + year + '/spring/' + course[0] + '/' + \
                     course[1] + '.xml?mode=cascade'
    credithoururl = urllib.request.urlopen(actuallink).read()
    creditsoup = BeautifulSoup(credithoururl)
    letters = creditsoup.find_all('credithours')
    letter = letters[0]
    credithours = str(letter)
    junk,credithours,junk=credithours.split('>')
    credithours, junk = credithours.split('h',maxsplit=1)
    #now create a link to the current page so people can check if there are registration spots open 
    courseLink = 'https://courses.illinois.edu/schedule/2018/spring/' + course[0] + '/' + course[1]
    #fill in the table row wrapper with all the relevant information
    new_table_row = htmlwrapper % (courseLink, whichcourse,course[2], totalKids, credithours, percent4, percentA)
    # write to the index page
    indexhtml.write(new_table_row)
    #now write to the various gen-ed webpages if the course is in that gen-eds list of classes
    x=0
    for page in listofwebpages[1:]:
        for item in classesListedByGened[x]:
            if whichcourse==item:
                page.write(new_table_row)
        x=x+1

# this is the same for every webpage; it closes the table and closes the page
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