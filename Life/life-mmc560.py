""" Assignment: Snake
    Created on 2 dec. 2020
    @author: Mark Melnic """

from ipy_lib3 import LifeUserInterface

WIDTH = 9
HEIGHT = 9

with open("LifeInput1.txt", "r") as input_file:
    lines = input_file.readlines()

gen_nr = int(lines.pop(0))
osc_nr = int(lines.pop(0))
board_cfg = []
for line in lines:
    temp = []
    for ch in line:
        if ch == " ":
            temp.append(0)
        elif ch == "x":
            temp.append(1)
    board_cfg.append(temp)

if __name__ == "__main__":
    root = LifeUserInterface(WIDTH, HEIGHT)
    for i, line in enumerate(board_cfg):
        for j, ch in enumerate(line):
            root.place(j, i, ch)
    root.show()
    root.stay_open()
