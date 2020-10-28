""" Assignment: geography grades 3
    Created on 28 oct. 2020
    @author: Mark Melnic """

with open("Module 4/Geography Grades 3/input.txt", "r") as input_file:
    lines = input_file.readlines()

    groups = []
    temp = []
    for line in lines:
        temp.append(line)
        if line == "=\n":
            groups.append(temp[:-1])
            temp = []
        if lines.index(line) == len(lines) - 1:
            groups.append(temp)

    for group in groups:
        print("Report for group %s" % group[0], end="")
        group.pop(0)
        for student in group:
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
                if average - int(average) < 0.25:
                    average = int(average)
                elif average - int(average) >= 0.25 and average - int(average) < 0.75:
                    average = int(average) + 0.5
                elif average - int(average) >= 0.75:
                    average = int(average) + 1
            else:
                if average - int(average) < 0.25:
                    average = int(average)
                elif average - int(average) >= 0.25 and average - int(average) < 0.75:
                    average = int(average) + 0.5
                else:
                    average = int(average) + 1
            if average >= 5.5 and average < 6:
                average = 6

            print("%s has an average grade of %.1f" % (name, average))

        print("End of report\n")
