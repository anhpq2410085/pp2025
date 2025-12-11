import curses
import input as ui_in
import output as ui_out


def main(stdscr):
    students = []
    courses = []
    ui_in.input_students(stdscr, students)
    ui_in.input_courses(stdscr, courses)

    while True:
        ui_out.draw_menu(stdscr, courses)

        choice_str = ui_in.safe_input(stdscr, "")

        if not choice_str.isdigit():
            continue

        choice = int(choice_str)

        if choice == 0:
            break
        if 1 <= choice <= len(courses):
            selected_course = courses[choice - 1]
            ui_in.input_marks(stdscr, students, selected_course)

    for s in students:
        s.calculate_gpa(courses)
    students.sort(key=lambda x: x.gpa, reverse=True)

    ui_out.show_final_results(stdscr, students)

if __name__ == "__main__":
    curses.wrapper(main)