""" Assignment: geography grades 2
    Created on 28 oct. 2020
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

        if average >= 5.5:
            if average >= 5.5 and average < 6:
                average = 6
            elif average - int(average) < 0.25:
                average = int(average)
            elif average - int(average) >= 0.25 and average - int(average) < 0.75:
                average = int(average) + 0.5
            elif average - int(average) >= 0.5:
                average = int(average) + 1
        else:
            if average - int(average) < 0.25:
                average = int(average)
            elif average - int(average) >= 0.25 and average - int(average) < 0.75:
                average = int(average) + 0.5

        print("%s has an average grade of %.1f" % (name, average))

    print("End of report")

