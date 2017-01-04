# GradeDistributionCourseExplorer

What the University doesn't want you to know: Sort classes by the percent of students that get A's!
link:

http://nkpatel6.web.engr.illinois.edu/

## Current Status

**Original Data Source:** FOIA requested data from Fall 2015 that lists all sections of all courses on campus and their grade distributions 

**Python**:Take the Fall15.csv file and strip out all class sections that don't give out actual grades (Discussions, Labs, recitals, lessons, etc.). Generate an output csv file with only data I actually care about, and an HTML file that stores everything in a basic, 1300 row, 4 column table. 

**HTML/CSS/JQUERY:** The final step is using a jQuery plugin called tablesorter that allowed me to turn my static HTML table into one that was sortable. A CSS style sheet completed the (albeit basic) look to allow for full functionality. The site is now hosted on my personal space at the University of Illinois.


##Future Features

I originally came up with this idea because I wanted to know which advanced composition class was the easiest. So, I'd like to create a nav bar that lets to sort by either Gen-Ed requirement or by subject. The data is already included in my output CSV file; this is just my first foray into making an actual website so I was unsure of how to do it. 

The second feature I wanted to add was the ability to click on a class (say, ECE120) and see grade distributions by professor. This way, for classes like CHEM102, people would be able to objectively decide which professor is harsher or more lenient then the other. 

I would also like to make the site (and the table) look much prettier! 