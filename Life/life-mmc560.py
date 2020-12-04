""" Assignment: Snake
    Created on 2 dec. 2020
    @author: Mark Melnic """

from ipy_lib3 import LifeUserInterface

WIDTH = 9
HEIGHT = 9

def surrounding(board, x, y):
    ret = []
    for ind_i in range(max(0, x-1), min(x+2, len(board))):
        for ind_j in range(max(0, y-1), min(y+2, len(board[0]))):
            if not (ind_i, ind_j) == (x, y):
                ret.append(int(board[ind_i][ind_j]))
    return ret

def check_neighbours(board, i, j):
    neighbours = surrounding(board, i, j)
    neigh_nr = sum(neighbours)

    item = board[i][j]
    if item == 0:
        if neigh_nr == 3:
            item = 1
    elif item == 1:
        if neigh_nr < 2:
            item = 0
        elif neigh_nr > 3:
            item = 0
    return item

with open("LifeInput3.txt", "r") as input_file:
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
    for i in range(gen_nr):
        root.clear()
        new_board_cfg = []
        for i, line in enumerate(board_cfg):
            temp_line = []
            for j, ch in enumerate(line):
                new_ch = check_neighbours(board_cfg, i, j)
                temp_line.append(new_ch)
                root.place(j, i, new_ch)
            new_board_cfg.append(temp_line)

        root.show()
        root.wait(100)
        board_cfg = new_board_cfg
