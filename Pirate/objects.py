X_SHIFT = 1

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
