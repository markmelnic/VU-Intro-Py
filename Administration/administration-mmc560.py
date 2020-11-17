""" Assignment: administration
    Created on 28 oct. 2020
    @author: Mark Melnic """


def name_grades(line):
    name = ""
    for ch in line:
        if not ch == "_":
            name += ch
        else:
            break

    grades = ""
    for ch in line[::-1]:
        if not ch == "_":
            grades += ch
        else:
            break

    grades = [float(g) for g in grades[::-1].split(" ")]

    average = sum(grades) / len(grades)
    if average >= 5.5 and average < 6:
        average = str(int(average) + 1) + "-"
    else:
        average_fractional = average - int(average)
        if average_fractional < 0.25:
            average = int(average)
        elif average_fractional >= 0.25 and average_fractional < 0.75:
            average = int(average) + 0.5
        else:
            average = int(average) + 1

    print("%s has an average of %s" % (name, str(average)))


def representation(line):
    similarities, names = line.split(";")

    graph = ""
    for num in similarities.split("="):
        if int(num) == 0:
            graph += "_"
        elif int(num) > 0 and int(num) < 20:
            graph += "-"
        elif int(num) >= 20:
            graph += "^"
    print("    %s" % graph, end="")

    names = names.split(",")
    if len(names) == 0 or names[0] == "":
        print("\n    No matches found", end="")
    else:
        for name in names:
            print("\n   ", name, end="")


if __name__ == "__main__":
    filename = str(input("What is the file name (withouth the .txt extension): "))
    if filename == "":
        filename = "input.txt"
    else:
        filename += ".txt"

    with open("Administration/" + filename, "r") as input_file:
        lines = input_file.readlines()

    for i, line in enumerate(lines):
        if i % 2 == 0:
            name_grades(line)
        else:
            representation(line)
