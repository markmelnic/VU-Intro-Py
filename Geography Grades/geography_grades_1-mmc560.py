""" Assignment: geography grades 1
    Created on 9 nov. 2020
    @author: Mark Melnic """


def average(grades):
    return sum(grades) / len(grades)


def get_name(line):
    return line.split("_")[0]


def get_grades(line):
    return line.split("_")[-1].split(" ")


def process_student(line: str):
    name = get_name(line)
    grades = get_grades(line)

    grades = [float(g) for g in grades]

    avg = average(grades)

    print("%s has an average grade of %.2f" % (name, avg))


with open("input.txt", "r") as input_file:
    students = input_file.readlines()

print("Report for group 2b")
for student in students:
    process_student(student)

print("End of report")
