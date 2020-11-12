""" Assignment: geography grades 1
    Created on 9 nov. 2020
    @author: Mark Melnic """

# calculate average grade
def average(grades):
    return sum(grades) / len(grades)

# get student name
def get_name(line):
    return line.split("_")[0]

# get student grades
def get_grades(line):
    return line.split("_")[-1].split(" ")

def process_student(line: str):
    name = get_name(line)
    grades = get_grades(line)

    # transform str grades into floats
    grades = [float(g) for g in grades]

    avg = average(grades)

    print("%s has an average grade of %.2f" % (name, avg))

# read input file
with open("input.txt", "r") as input_file:
    students = input_file.readlines()

print("Report for group 2b")
# process each student
for student in students:
    process_student(student)

print("End of report")
