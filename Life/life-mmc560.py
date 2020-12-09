""" Assignment: Snake
    Created on 4 dec. 2020
    @author: Mark Melnic """

from Life.logic import Logic

def load_file():
    filename = str(input("Type the filename to load here: "))
    with open(filename, "r") as input_file:
        return input_file.readlines()

def load_data(file_contents):
    gen_nr = int(file_contents.pop(0))
    osc_nr = int(file_contents.pop(0))
    board_config = []
    for line in file_contents:
        temp = []
        for ch in line:
            if ch == " ":
                temp.append(0)
            elif ch == "x":
                temp.append(1)
        board_config.append(temp)
    return gen_nr, osc_nr, board_config

if __name__ == "__main__":
    file_contents = load_file()
    life_game = Logic(load_data(file_contents))
