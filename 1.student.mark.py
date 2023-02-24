students = []
courses = []
marks = {}

#input students information
def input_students():
    num_students = int(input("Enter the number of students: "))
    for i in range(num_students):
        student_name = input("Enter the name of student: ")
        student_id = input("Enter the id of student: ")
        student_dob = input("Enter the day of birth of student: ")
        students.append((student_name,student_id,student_dob))

# input courses information
def input_courses():
    num_courses = int(input("Enter the number of course: "))
    for i in range(num_courses):
        course_name = input("Enter the name of course: ")
        course_id = input("Enter the id of course: ")
        courses.append((course_name, course_id))

# input student mark in course base on id
def input_marks():
    for course in courses:
        if course in courses:
            for student in students:
                if student in students:
                    course_id = input("Enter the course name to enter mark: ")
                    student_id = input("Enter the student id to enter mark: ")
                    mark = input("Mark for student in course: ")
                    marks[student_id,course_id] = mark
                    return
                else:
                    print("incorrect id")
                    break
        print("incorrect id")
        break
    print("mark: ", marks)


# Display a list
def list_students():
    for student in students:
        print(f" name:{student[0]} - id:{student[1]} - dob:{student[2]} ")

def list_courses():
    print("course")
    for course in courses:
        print(f" name:{course[0]} - id:{course[1]} ")


#option for system
while(True):
    print("0.Exit")
    print("1. input students")
    print("2. input courses")
    print("3. input marks for student")
    print("4. list student")
    print("5. list course")
    selection = int(input("Enter your select: "))
    if selection == 0:
        break
    elif selection == 1:
        input_students()
    elif selection == 2:
        input_courses()
    elif selection == 3:                     
        input_marks()
    elif selection == 4:       
        list_students()
    elif selection == 5:
        list_courses()
    else:
        print("invalid input. please try again")