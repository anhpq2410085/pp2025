def draw_menu(stdscr, courses):
    stdscr.clear()
    stdscr.addstr(0, 0, "Student management system")
    for idx, c in enumerate(courses):
        stdscr.addstr(idx + 2, 0, f"{idx + 1}. {c.name}")

    row = len(courses) + 3
    stdscr.addstr(row, 0, "0. Exit and sort")
    stdscr.addstr(row + 2, 0, "Select course: ")
    stdscr.refresh()

def show_final_results(stdscr, students):
    stdscr.clear()
    stdscr.addstr(0, 0, f"{'ID':<10}{'Name':<20}{'GPA':<10}")
    stdscr.addstr(1, 0, "-" * 40)
    for idx, s in enumerate(students):
        stdscr.addstr(idx + 2, 0, f"{s.id:<10}{s.name:<20}{s.gpa:.2f}")

    stdscr.addstr(len(students) + 4, 0, "Press any key to exit")
    stdscr.refresh()
    stdscr.getch()