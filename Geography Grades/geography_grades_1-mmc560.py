""" Assignment: geography grades 1
    Created on 9 nov. 2020
    @author: Mark Melnic """

def process_student(line: str):
    split_line = line.split("_")
    name = split_line[0]
    grades = split_line[-1]

    grades = grades.split(" ")
    grades = [float(g) for g in grades]

    average = sum(grades) / len(grades)

    print("%s has an average grade of %.2f" % (name, average))


with open("Geography Grades/input.txt", "r") as input_file:
    students = input_file.readlines()

print("Report for group 2b")
for student in students:
    process_student(student)

print("End of report")
