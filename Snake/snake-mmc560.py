""" Assignment: Snake
    Created on 2 dec. 2020
    @author: Mark Melnic """

from ipy_lib3 import SnakeUserInterface

ANIMATION_SPEED = 4
WIDTH = 32
HEIGHT = 24

def read_level():
    walls = []
    filename = str(input(
            "Do you have a level to load? Type the file name here, otherwise just press ENTER: "))
    if not filename == "":
        with open(filename, "r") as level:
            content = level.read().split("=")
            event_data = content[1].lower()

            snake_pos = []
            for pos in content[0][::-1].split("\n"):
                pos = pos.split()
                snake_pos.append((int(pos[0]), int(pos[1])))

            for pos in content[2][:-1].split("\n"):
                pos = pos.split()
                walls.append((int(pos[0]), int(pos[1])))
    else:
        snake_pos = [(0, 0), (1, 0)]
        event_data = "r"
    return snake_pos, event_data, walls

class Logic():
    def __init__(self, root):
        self.root = root
        self.root.set_animation_speed(ANIMATION_SPEED)
        self.event_name = "arrow"
        self.snake_pos, self.event_data, self.walls = read_level()
        self.run()

    def run(self, ):
        self.generate_food()
        self.running = True
        while self.running:
            self.display()
            self.event = self.root.get_event()
            self.check_arrow_event()
            if self.event.data == "refresh":
                self.check_event_direction()
                if self.check_position():
                    self.move()
                    self.check_food()

    def display(self, ):
        self.root.clear()
        self.root.place(self.food[0], self.food[1], 1)
        for pos in self.snake_pos:
            self.root.place(pos[0], pos[1], 2)
        for pos in self.walls:
            self.root.place(pos[0], pos[1], 3)
        self.root.show()

    def generate_food(self, ):
        self.food = (self.root.random(WIDTH), self.root.random(HEIGHT))
        while self.food in self.snake_pos or self.food in self.walls:
            self.food = (self.root.random(WIDTH), self.root.random(HEIGHT))

    def move(self, ):
        for i, piece in enumerate(self.snake_pos):
            piece = list(piece)
            if piece[0] == -1:
                piece[0] = WIDTH - 1
                self.snake_pos[i] = tuple(piece)
            elif piece[0] == WIDTH:
                piece[0] = 0
                self.snake_pos[i] = tuple(piece)
            if piece[1] == -1:
                piece[1] = HEIGHT - 1
                self.snake_pos[i] = tuple(piece)
            elif piece[1] == HEIGHT:
                piece[1] = 0
                self.snake_pos[i] = tuple(piece)

    def check_event_direction(self, ):
        if self.event_data == "r":
            self.snake_pos.append((self.snake_pos[-1][0] + 1, self.snake_pos[-1][1]))
        elif self.event_data == "l":
            self.snake_pos.append((self.snake_pos[-1][0] - 1, self.snake_pos[-1][1]))
        elif self.event_data == "u":
            self.snake_pos.append((self.snake_pos[-1][0], self.snake_pos[-1][1] - 1))
        elif self.event_data == "d":
            self.snake_pos.append((self.snake_pos[-1][0], self.snake_pos[-1][1] + 1))

    def check_arrow_event(self, ):
        if self.event.name == "arrow" and (
            (self.event_data == "r" and not self.event.data == "l") or
            (self.event_data == "l" and not self.event.data == "r") or
            (self.event_data == "u" and not self.event.data == "d") or
            (self.event_data == "d" and not self.event.data == "u")
        ):
            self.event_name = self.event.name
            self.event_data = self.event.data

    def check_position(self, ):
        if len(self.snake_pos) != len(set(self.snake_pos)) or any(pos in self.walls for pos in self.snake_pos):
            self.root.clear_text()
            self.root.print_("Game over")
            self.running = False
            self.root.stay_open()
            return self.running
        else:
            return self.running

    def check_food(self, ):
        if self.snake_pos[-1] == self.food:
            self.generate_food()
        else:
            self.snake_pos.pop(0)

if __name__ == "__main__":
    snake_game = Logic(SnakeUserInterface(WIDTH, HEIGHT))
