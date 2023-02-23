#input function
def input_students():
    students = []
    num_students = input("Enter the number of students: ")
    for i in range(num_students):
        student_name = input("Enter the name of student: ")
        student_id = input("Enter the id of student: ")
        student_dob = input("Enter the day of birth of student: ")
        students.append(student_name,student_id,student_dob)

def input_courses():
    courses = []
    num_courses = input("Enter the number of course: ")
    for i in range(num_course):
        course_name = input("Enter the name of course: ")
        course_id = input("Enter the id of course: ")
        course.append(course_name, course_id)

def input_marks(student_id, course_id):
    marks = {}
    prompt = f"Enter marks for student {student_id} for course {course_id}: ".format (student_id, course_id)
    input (prompt)
    for i in range (students):
        students.append ((student_name,student_id,student_dob))
        for i in range (courses):
            course.append((course_name, course_id))
    n = int (input ("Enter how many student-course marks do you want to enter? ")) 
        for i in range (n):     
            while True:         
                student_id = input ("Enter student id: ")         
                course_id = input ("Enter course id: ")         
                if student_id not in [student [0] for student in students]:             
                    print ("Bad student id")             
                    continue          
                    if courseid not in [course [0] for course in courses]:             
                        print ("Bad course id")             
                        continue          
                        break     
                        marks = int (input ("Enter marks: "))     
                        if course_id in mark:         
                            mark [course_id].append ((student_id, marks))     
                            else:         
                                d [coure_id] = [(student_id, marks)]

# Display a list of students

while(True):
    print("\n0. Exit")
    print("1. Input students")                      #option 0-6
    print("2. Input courses")
    print("3. Input marks")
    print("4. List student infor")
    print("5. List course infor")
    print("6. Show marks for a given course")
    choose = int(input("Enter your choice: "))
    if choose == 0:                                 
        break
    elif choose == 1:                               #choose 1 to input student infor
        input_students_infor()
    elif choose == 2:                               #choose 2 to input courses infor
        input_courses_infor()
    elif choose == 3:                               #choose 3 to input student mark
        input_marks()
    elif choose == 4:                               #choose 4 to list student infor
        list_students()
    elif choose == 5:                               #choose 5 to list course infor
        list_courses()
    elif choose == 6:                               #choose 6 to list student mark
        list_marks()
    else:
        print("Invalid, please choose one obtion above:")