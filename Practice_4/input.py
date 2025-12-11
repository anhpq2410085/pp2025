import math
import curses
from domains.student import Student
from domains.course import Course

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


def input_students(stdscr, students):
    stdscr.clear()
    stdscr.addstr(0, 0, "Input Number of Students: ")
    stdscr.refresh()

    try:
        n_str = safe_input(stdscr, "")
        n = int(n_str)
    except ValueError:
        n = 0

    for i in range(n):
        stdscr.clear()
        stdscr.addstr(0, 0, f"Student {i + 1}")
        sid = safe_input(stdscr, "ID: ", 2, 0)
        name = safe_input(stdscr, "Name: ", 3, 0)
        dob = safe_input(stdscr, "DoB: ", 4, 0)
        students.append(Student(sid, name, dob))


def input_courses(stdscr, courses):
    stdscr.clear()
    stdscr.addstr(0, 0, "Input Number of Courses: ")
    stdscr.refresh()

    try:
        n_str = safe_input(stdscr, "")
        n = int(n_str)
    except ValueError:
        n = 0
    for i in range(n):
        stdscr.clear()
        stdscr.addstr(0, 0, f"--- Course {i + 1} ---")
        cid = safe_input(stdscr, "ID: ", 2, 0)
        name = safe_input(stdscr, "Name: ", 3, 0)
        try:
            cred_str = safe_input(stdscr, "Credits: ", 4, 0)
            cred = int(cred_str)
        except ValueError:
            cred = 0
        courses.append(Course(cid, name, cred))
def input_marks(stdscr, students, selected_course):
    for s in students:
        stdscr.clear()
        stdscr.addstr(0, 0, f"Marking Course: {selected_course.name}")
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