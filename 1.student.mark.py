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

