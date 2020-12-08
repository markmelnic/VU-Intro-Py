""" Assignment: pirate
    Created on 24 nov. 2020
    @author: Mark Melnic """

X_SHIFT = 1
DEFAULT_INPUT_FILE = "PirateInput.txt"
OUTPUT_FILE = "PirateOutput.txt"

class Coordinate:
    def __init__(self, item):
        self.x = int(item.split(",")[0]) + X_SHIFT
        self.y = int(item.split(",")[1])

    def __repr__(self):
        return "{},{}".format(self.x, self.y)

class CoordinateRow:
    def __init__(self, row):
        self.coords = [Coordinate(item) for item in row.split()]

    def interlace(self, new_row):
        interlations = max(len(self.coords), len(new_row.coords))
        temp_coords = []
        for i in range(interlations):
            if len(self.coords) > i:
                temp_coords.append(self.coords[i])
            if len(new_row.coords) > i:
                temp_coords.append(new_row.coords[i])
        self.coords = temp_coords

def read_input():
    filename = str(input("What file would you like to process (leave empty for default %s): " % DEFAULT_INPUT_FILE))
    if filename == "":
        filename = DEFAULT_INPUT_FILE
    with open(filename, "r") as input_file:
        return input_file.read().split("=")

def write_output(coordinates):
    with open(OUTPUT_FILE, "w") as output_file:
        print("The coordinates are:")
        for coordinate in coordinates:
            print(coordinate)
            output_file.write(str(coordinate) + "\n")
    print("You may also check the output file %s." % OUTPUT_FILE)

if __name__ == "__main__":
    input_content = read_input()
    all_coordinates = CoordinateRow(input_content.pop(0))
    for row in input_content:
            all_coordinates.interlace(CoordinateRow(row))
    write_output(all_coordinates.coords)
