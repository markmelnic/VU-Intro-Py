""" Assignment: administration
    Created on 17 nov. 2020
    @author: Mark Melnic """


def name_grades(line):
    name, grades = list(filter(lambda item: item != "", line.split("_")))

    grades = [float(g) for g in grades.split(" ")]

    average = get_average(grades)

    print("%s has an average of %s" % (name, str(average)))


def representation(line):
    similarities, names = line.split(";")

    graph = generate_graph(similarities)
    print("    %s" % graph, end="")

    names = names.split(",")
    if len(names) == 0 or names[0] == "":
        print("\n    No matches found", end="")
    else:
        for name in names:
            print("\n   ", name, end="")


def generate_graph(similarities):
    graph = ""
    for number in similarities.split("="):
        if int(number) == 0:
            graph += "_"
        elif int(number) > 0 and int(number) < 20:
            graph += "-"
        elif int(number) >= 20:
            graph += "^"
    return graph


def get_average(grades):
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
    return str(average)


if __name__ == "__main__":
    filename = str(input("What is the file name (leave empty if \"input.txt\"): "))
    if filename == "":
        filename = "input.txt"

    with open(filename, "r") as input_file:
        lines = input_file.readlines()

    for i, line in enumerate(lines):
        if i % 2 == 0:
            name_grades(line)
        else:
            representation(line)
