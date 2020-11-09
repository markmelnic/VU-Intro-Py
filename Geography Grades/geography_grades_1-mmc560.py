""" Assignment: geography grades 1
    Created on 9 nov. 2020
    @author: Mark Melnic """

with open("input.txt", "r") as input_file:
    students = input_file.readlines()

    print("Report for group 2b")
    for student in students:
        name = ""
        for ch in student:
            if not ch == "_":
                name += ch
            else:
                break

        grades = ""
        for ch in student[::-1]:
            if not ch == "_":
                grades += ch
            else:
                break

        grades = grades[::-1].split(" ")
        grades = [float(g) for g in grades]
        average = sum(grades) / len(grades)

        print("%s has an average grade of %.2f" % (name, average))

    print("End of report")
