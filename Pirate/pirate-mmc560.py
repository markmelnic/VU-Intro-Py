""" Assignment: pirate
    Created on 24 nov. 2020
    @author: Mark Melnic """


class Coordinate:
    def __init__(self, item):
        self.x = int(item.split(",")[0]) + 1
        self.y = int(item.split(",")[1])
        self.coord = str(self.x) +","+ str(self.y)
    def __repr__(self):
        return "{}".format(self.coord)


class CoordinateRow:
    def __init__(self, row):
        if type(row) == str:
            self.coords = [Coordinate(item) for item in row.split()]
        else:
            self.coords = [Coordinate(item) for item in row]
    def __repr__(self):
        c_str = ""
        for c in self.coords:
            c_str += "{} ".format(c)
        return "Coordinates are: {}".format(c_str)

    def interlace(self, new_row):
        temp_coords = []
        for i in range(max(len(self.coords), len(new_row.coords))):
            try:
                temp_coords.append(self.coords[i])
            except IndexError:
                pass
            try:
                temp_coords.append(new_row.coords[i])
            except IndexError:
                pass
        self.coords = temp_coords


if __name__ == "__main__":
    with open("PirateInput.txt", "r") as input_file:
        rows = input_file.read().split("=")
    
    all_coordinates = []
    for i, row in enumerate(rows):
        if not i == 0:
            all_coordinates.interlace(CoordinateRow(row))
        else:
            all_coordinates = CoordinateRow(row)

    print("The path is:")
    for c in all_coordinates.coords:
        print(c)
