""" Assignment: pirate
    Created on 24 nov. 2020
    @author: Mark Melnic """


class Coordinate:
    def __init__(self, item):
        self.x = int(item.split(",")[0]) + 1
        self.y = int(item.split(",")[1])

    def __repr__(self):
        return "{},{}".format(self.x, self.y)


class CoordinateRow:
    def __init__(self, row):
        self.coords = [Coordinate(item) for item in row.split()]

    def __repr__(self):
        c_str = ""
        for c in self.coords:
            c_str += "{} ".format(c)
        return "This row has the following coordinates: {}".format(c_str)

    def interlace(self, new_row):
        temp_coords = []
        interlations = max(len(self.coords), len(new_row.coords))
        for i in range(interlations):
            try:
                temp_coords.append(self.coords[i])
            except IndexError:
                pass
            try:
                temp_coords.append(new_row.coords[i])
            except IndexError:
                pass
        self.coords = temp_coords


def read_input():
    with open("PirateInput.txt", "r") as input_file:
        return input_file.read().split("=")


def write_output(coordinates):
    with open("PirateOutput.txt", "w") as output_file:
        for coordinate in coordinates:
            print(coordinate)
            output_file.write(str(coordinate) + "\n")


if __name__ == "__main__":
    all_coordinates = []
    for i, row in enumerate(read_input()):
        if i == 0:
            all_coordinates = CoordinateRow(row)
        else:
            all_coordinates.interlace(CoordinateRow(row))

    write_output(all_coordinates.coords)
