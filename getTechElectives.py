def get_tech_elective_list():

    read_file = open('tech_electives')
    full_list=[]
    for line in read_file.readlines():
        line=line.rstrip('\n')
        raw=line.split('(')
        course_number,courses=raw[1].split(': ')
        course_number=course_number[:-1]
        courses=courses.split(', ')
        for i in range(0,len(courses)):
            courses[i].lstrip()
            courses[i]=course_number+courses[i]
            full_list.append(courses[i])
    return(full_list)

if __name__ == "__main__":
    get_tech_elective_list()