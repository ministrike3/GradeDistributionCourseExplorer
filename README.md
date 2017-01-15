# GradeDistributionCourseExplorer

Get a better GPA: Sort classes by the percent of students that get A's!
link:

http://nkpatel6.web.engr.illinois.edu/

## Current Status

**Original Data Source:** FOIA requested data from Fall 2015 that lists all sections of all courses on campus and their grade distributions 

**Python:**Take the Fall15.csv file and strip out all class sections that don't give out actual grades (Discussions, Labs, recitals, lessons, etc.). Generate an output csv file with only data I actually care about, and an HTML file that stores everything in a basic, 1300 row, 4 column table.

**HTML/CSS/JQUERY:** The final step is using a jQuery plugin called tablesorter that allowed me to turn my static HTML table into one that was sortable. A CSS style sheet completed the (albeit basic) look to allow for full functionality. The site is now hosted on my personal space at the University of Illinois, linked above.


##Future Features

Create a Searchbar to look for specific classes (Please use Control+F for now)

Click on class and see grade distributions by professor.

##Changelog

**1/14/17:** Complete overhaul of python script: Did it get faster? Not sure, but its definitely much prettier code that I'm happier with; the old version worked well but was doing lots of unnecessary things (writing to csv, doing things over and over statically rather then in a loop, etc.) Had a few problems, asked around + posted on Stack Overflow. One more overhaul will be done eventually to replace all lists with a dictionary for a much cleaner data cleaning process. 

**1/11/17:** Removed HTML from the Repo because this is a python project first; the webpage is simply to display the data. Plus the webpage is linked at the top of this readme anyway!  

**1/6/17:** Edited Python Script to allow for multiple semesters of data to be used for more accuracy and a more comprehensive course list. Script rewrite in progress; adding the multiple semesters feature was copied and pasted from my complete rewrite. 

**1/5/17:**Each course number is now linked to the course explorer site so visitors can navigate there for more info

**1/5/17:**Added a column for the names of classes, not just course numbers. 

**1/5/17:** Added new pages to the site + a navigation bar to allow people to look at classes that fulfill certain Gen-Ed requirements

**1/4/17:** Added Credit Hours

