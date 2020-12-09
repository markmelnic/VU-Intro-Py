""" Assignment: pirate
    Created on 24 nov. 2020
    @author: Mark Melnic """

from Pirate.objects import *

DEFAULT_INPUT_FILE = "PirateInput.txt"
OUTPUT_FILE = "PirateOutput.txt"

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
