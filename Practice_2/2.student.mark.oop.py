class Student:
    def __init__(self, student_id, name, dob):
        self.id = student_id
        self.name = name
        self.dob = dob

    def __str__(self):
        return f"{self.id}, {self.name}, {self.dob}"

class Course:
    def __init__(self, course_id, name, students):
        self.id = course_id
        self.name = name
        self.students = students
        self.marks = {}

    def input_marks(self):
        print(f"\n-Mark Course: {self.name}")
        for student in self.students:
            while True:
                try:
                    mark = float(input(f"Enter student {student.name} mark in course {self.name}: "))
                    self.marks[student.id] = mark
                    break
                except ValueError:
                    print("Please enter a number.")

    def print_marks(self):
        print("Name, Mark")
        for student in self.students:
            mark = self.marks.get(student.id, 0)
            print(f"{student.name}, {mark}")

class SchoolManagement:
    def __init__(self):
        self.students = []
        self.courses = []

    def input_students(self):
        while True:
            try:
                num_students = int(input("Enter number of students: "))
                break
            except ValueError:
                print("Please input an integer.")

        print("\nStudent Information")
        for i in range(num_students):
            while True:
                try:
                    s_id = input(f"Enter student {i + 1} ID: ")
                    s_name = input(f"Enter student {i + 1} Name: ")
                    s_dob = input(f"Enter student {i + 1} DoB: ")
                    self.students.append(Student(s_id, s_name, s_dob))
                    break
                except Exception:
                    print("Invalid input .")

    def input_courses(self):
        print("\nCourse Information")
        while True:
            try:
                num_courses = int(input("Enter number of courses: "))
                break
            except ValueError:
                print("Please enter an integer.")
        for i in range(num_courses):
            c_id = input(f"Enter course {i + 1} ID: ")
            c_name = input(f"Enter course {i + 1} Name: ")
            self.courses.append(Course(c_id, c_name, self.students))

    def select_course_and_mark(self):
        print("\nList Course")
        for index, course in enumerate(self.courses):
            print(f"ID: {course.id} - Tên: {course.name}")

        selected_course = None
        while selected_course is None:
            try:
                choice = int(input(f"\nEnter the NUMBER [1 - {len(self.courses)}] of the course you want to choose: "))
                if 1 <= choice <= len(self.courses):
                    selected_course = self.courses[choice - 1]
                else:
                    print(f"Please choose an integer from 1 to {len(self.courses)}.")
            except ValueError:
                print("Please enter an integer")

        selected_course.input_marks()
        return selected_course

    def print_student_list(self):
        print("\nID", "Name", "Date_of_birth")
        for s in self.students:
            print(s)

    def print_course_list(self):
        print("\n{:<5} {:<20}".format ("ID", "Course"))
        for c in self.courses:
            print (f"{c.id}, {c.name}")

sm = SchoolManagement()
sm.input_students()
sm.input_courses()
graded_course = sm.select_course_and_mark()

sm.print_student_list()
sm.print_course_list()

print("\nMarks")
if graded_course:
    graded_course.print_marks()