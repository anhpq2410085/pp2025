import math
import numpy as np
import curses

class Student:
    def __init__(self, student_id, name, dob):
        self.id = student_id
        self.name = name
        self.dob = dob
        self.gpa = 0.0
        self.marks = {}

class Course:
    def __init__(self, course_id, name, credits):
        self.id = course_id
        self.name = name
        self.credits = credits

class SchoolManagement:
    def __init__(self):
        self.students = []
        self.courses = []
    def add_student(self, student):
        self.students.append(student)
    def add_course(self, course):
        self.courses.append(course)
    def calculate_gpa(self):
        for student in self.students:
            marks = []
            credits = []
            for course in self.courses:
                if course.id in student.marks:
                    marks.append(student.marks[course.id])
                    credits.append(course.credits)
            if marks:
                np_marks = np.array(marks)
                np_credits = np.array(credits)
                if np.sum(np_credits) > 0:
                    student.gpa = np.average(np_marks, weights=np_credits)
                else:
                    student.gpa = 0.0
            else:
                student.gpa = 0.0

        self.students.sort(key=lambda x: x.gpa, reverse=True)

def safe_input(stdscr, prompt, y=None, x=None):
    if y is not None and x is not None:
        stdscr.move(y, x)
    stdscr.addstr(prompt)
    stdscr.refresh()
    curses.echo()
    curses.flushinp()
    try:
        input_bytes = stdscr.getstr()
        return input_bytes.decode('utf-8').strip()
    except:
        return ""
def main(stdscr):
    sm = SchoolManagement()

    stdscr.clear()
    stdscr.addstr(0, 0, "Input the number of students: ")
    stdscr.refresh()

    try:
        n_students_str = safe_input(stdscr, "")
        n_students = int(n_students_str)
    except ValueError:
        n_students = 0

    for i in range(n_students):
        stdscr.clear()
        stdscr.addstr(0, 0, f"Student {i + 1} ")
        sid = safe_input(stdscr, "ID: ", 2, 0)
        name = safe_input(stdscr, "Name: ", 3, 0)
        dob = safe_input(stdscr, "DoB: ", 4, 0)
        sm.add_student(Student(sid, name, dob))

    stdscr.clear()
    stdscr.addstr(0, 0, "Input the number of courses: ")
    stdscr.refresh()

    try:
        n_courses_str = safe_input(stdscr, "")
        n_courses = int(n_courses_str)
    except ValueError:
        n_courses = 0

    for i in range(n_courses):
        stdscr.clear()
        stdscr.addstr(0, 0, f"Course {i + 1} ")
        cid = safe_input(stdscr, "ID: ", 2, 0)
        name = safe_input(stdscr, "Name: ", 3, 0)
        try:
            credits_str = safe_input(stdscr, "Credits: ", 4, 0)
            credits = int(credits_str)
        except ValueError:
            credits = 0
        sm.add_course(Course(cid, name, credits))

    while True:
        stdscr.clear()
        stdscr.addstr(0, 0, "Student management system")
        for idx, c in enumerate(sm.courses):
            stdscr.addstr(idx + 2, 0, f"{idx + 1}. {c.name}")

        row = len(sm.courses) + 3
        stdscr.addstr(row, 0, "0: Exit and sort GPA")

        choice_str = safe_input(stdscr, "Select course: ", row + 2, 0)

        if not choice_str.isdigit():
            continue
        choice = int(choice_str)

        if choice == 0:
            break
        if 1 <= choice <= len(sm.courses):
            selected_course = sm.courses[choice - 1]

            for s in sm.students:
                stdscr.clear()
                stdscr.addstr(0, 0, f"Marking {selected_course.name}")
                while True:
                    raw_str = safe_input(stdscr, f"Mark for {s.name}: ", 2, 0)
                    try:
                        raw = float(raw_str)
                        final_mark = math.floor(raw * 10) / 10
                        s.marks[selected_course.id] = final_mark
                        break
                    except ValueError:
                        stdscr.addstr(4, 0, "Invalid number. Try again.")
                        stdscr.refresh()

    sm.calculate_gpa()
    stdscr.clear()
    stdscr.addstr(0, 0, f"{'ID':<10}{'Name':<20}{'GPA':<10}")
    stdscr.addstr(1, 0, "-" * 40)

    for idx, s in enumerate(sm.students):
        stdscr.addstr(idx + 2, 0, f"{s.id:<10}{s.name:<20}{s.gpa:.2f}")

    stdscr.addstr(len(sm.students) + 4, 0, "Press any key to exit")
    stdscr.refresh()
    stdscr.getch()
if __name__ == "__main__":
    curses.wrapper(main)