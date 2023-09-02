class Course :
    def __init__(self , course_id , course_name , course_level) :
        self.course_id = course_id
        self.course_name = course_name
        self.course_level = course_level


class Student :

    student_counter = 1

    def __init__(self , student_name , student_level ):
        self.student_id = Student.student_counter
        Student.student_counter += 1
        self.student_name = student_name
        self.student_level = student_level
        self.student_course = ()


    def add_course(self,course):
        if self.student_level == course.course_level :
            self.student_course.append(course)
            print(f"added course'{course.course_name}'to student'{self.student_name}'")

        else:
            print("cannot add a course of a different level to this student")


    def display_details(self):
        print("student details:")
        print(f"name:{self.student_name}")
        print(f"class:{self.student_level}")
        if self.student_course:
            print("course enrolled:")
            for course in self.student_course:
                print(f"-{course.course_name}(level{course.course_level})")

        else:
            print("no course enrolled")


    course = [Course(1 , "math", "A" ), (2 , "science" , "B")]
    students = []



while True:
    print("\n1.add new student")
    print("2.remove student")
    print("3.edit student")
    print("4.display all student")
    print("5.create new course")
    print("6.add course to student")
    print("7.exit")
    choice = input("enter your choice :")

    if choice == "1":
        new_student_name  = input("enter student name :")
        new_student_level = None
        while new_student_level not in ["A", "B", "C"]:
            new_student_level = input("select student level(A/B/C):").upper()

            if new_student_level not in ["A", "B", "C"]:
                print("invalid level.please select A,B or C")

        new_student = Student(new_student_name , new_student_level)

        print("student saved successfully")


    elif choice == "2":
        student_id = int(input("enter student id :"))
        student_to_remove = None
        for student in students :
            if student.student_id == student_id:
                student_to_remove = student
                break
        if student_to_remove:
            student.remove(student_to_remove)
            print(f"Student'{student_to_remove.student_name}' deleted successfully")

        else:
            print("student not found")

    elif choice == "3":
        student_id = int(input("enter student id:"))
        student_to_edit = None
        for student in students :
            if student.student_id == student_id :
                student_to_edit = student
                break
        if student_to_edit:
            new_name = input("enter new name :")
            new_level = None
            while new_level not in ["A", "B", "C"]:
                new_level = input("select new level (A/B/C):").upper()
                if new_level not in ["A", "B", "C"]:
                    print("invalid level.please select A ,B ,C ")
                    student_to_edit.student_name = new_name
                    student_to_edit.student_level = new_level
                    print("student information updated successfully")
                else:
                    print("student not found")

        elif choice == "4":
            for student in students:
                student.display_details()


        elif choice == "5":
            course_name = input("enter course name ")
            course_level = None
            while course_level not in ["A", "B", "C"]:
                course_level = input("select course level(A/b/C):").upper()
                if course_level not in ["A", "B", "C"]:
                    print("invalid level.please select course level (A,B,C)")
                    new_course_id = len(courses) + 1
                    new_course = Coruse(course_name, course_level)
                    courses.append(new_course)
                    print("new course added")



        elif choice == "6":
            student_id_enroll = int(input("enter student id :"))
            student_to_level_enroll =  input("enter student level :")
            course_id_enroll = int(input("enter course id :"))
            student_to_enroll = None
            course_to_enroll = None

            for student in students :
                if student.student_id == student_id_enroll :
                    student_to_enroll = student
                    break

            for course in courses :
                if course.course_id == course_id_enroll :
                    course_to_enroll = course
                    break
            if student_to_enroll and course_to_enroll :
                student_to_enroll.add_course(course_to_enroll)
            else:
                print("enter valid ids")

        elif choice == "7":
            print("exiting the program")

        else:
            print("enter a valid option")



