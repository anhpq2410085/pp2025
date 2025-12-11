import numpy as np

class Student:
    def __init__(self, student_id, name, dob):
        self.id = student_id
        self.name = name
        self.dob = dob
        self.gpa = 0.0
        self.marks = {}
    def calculate_gpa(self, courses):
        marks_list = []
        credits_list = []

        for course in courses:
            if course.id in self.marks:
                marks_list.append(self.marks[course.id])
                credits_list.append(course.credits)

        if marks_list:
            np_marks = np.array(marks_list)
            np_credits = np.array(credits_list)

            if np.sum(np_credits) > 0:
                self.gpa = np.average(np_marks, weights=np_credits)
            else:
                self.gpa = 0.0
        else:
            self.gpa = 0.0
    def __str__(self):
        return f"{self.id:<10} {self.name:<20} {self.dob:<15} {self.gpa:.2f}"