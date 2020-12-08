""" Assignment: Snake
    Created on 4 dec. 2020
    @author: Mark Melnic """

from ipy_lib3 import LifeUserInterface

WIDTH = 9
HEIGHT = 9

def load_file():
    filename = str(input("Type the filename to load here: "))
    with open(filename, "r") as input_file:
        return input_file.readlines()

def load_data(root, file_contents):
    gen_nr = int(file_contents.pop(0))
    osc_nr = int(file_contents.pop(0))
    board_config = []
    for line in file_contents:
        temp = []
        for ch in line:
            if ch == " ":
                temp.append(root.DEAD)
            elif ch == "x":
                temp.append(root.ALIVE)
        board_config.append(temp)
    return gen_nr, osc_nr, board_config

class Logic():
    def __init__(self, root, file_contents):
        self.root = root
        self.gen_nr, self.osc_nr, self.board = load_data(self.root, file_contents)
        self.run()

    def run(self, ):
        for i in range(self.gen_nr):
            self.root.clear()
            self.board = self.next_iteration()
            self.root.show()
            self.root.wait(100)
        self.oscillator_check()

    def oscillator_check(self, ):
        first_cfg = self.board
        for i in range(self.osc_nr):
            if i == 1 and first_cfg == self.board:
                self.root.print_("Static figure\n")
                break
            elif first_cfg == self.board:
                self.root.print_("Oscillating figure\n")
                break
            self.board = self.next_iteration()
        self.root.stay_open()

    def surrounding(self, x, y):
        surrounding = []
        for ind_i in range(max(0, x-1), min(x+2, len(self.board))):
            for ind_j in range(max(0, y-1), min(y+2, len(self.board[0]))):
                if not (ind_i, ind_j) == (x, y):
                    surrounding.append(int(self.board[ind_i][ind_j]))
        return surrounding

    def check_neighbours(self, i, j):
        neighbours = self.surrounding(i, j)
        neigh_nr = sum(neighbours)

        item = self.board[i][j]
        if item == self.root.DEAD:
            if neigh_nr == 3:
                item = self.root.ALIVE
        elif item == self.root.ALIVE:
            if neigh_nr < 2:
                item = self.root.DEAD
            elif neigh_nr > 3:
                item = self.root.DEAD
        return item

    def next_iteration(self, ):
        new_board = []
        for i, line in enumerate(self.board):
            temp_line = []
            for j, ch in enumerate(line):
                new_ch = self.check_neighbours(i, j)
                temp_line.append(new_ch)
                self.root.place(j, i, new_ch)
            new_board.append(temp_line)
        return new_board

if __name__ == "__main__":
    file_contents = load_file()
    life_game = Logic(LifeUserInterface(WIDTH, HEIGHT), file_contents)
