from ipy_lib3 import SnakeUserInterface

WIDTH = 32
HEIGHT = 24
ANIMATION_SPEED = 4

class Logic():
    def __init__(self, level):
        self.root = SnakeUserInterface(WIDTH, HEIGHT)
        self.root.set_animation_speed(ANIMATION_SPEED)
        self.snake_pos, self.event_data, self.walls = level
        self.running = True
        self.start()
        self.run()
        self.root.stay_open()

    def start(self, ):
        self.root.print_("Press any key to start!")
        while self.running:
            self.event = self.root.get_event()
            if self.event.name == "other":
                self.root.clear_text()
                break

    def run(self, ):
        self.generate_food()
        while self.running:
            self.display()
            self.event = self.root.get_event()
            self.check_arrow_event()
            if self.event.data == "refresh":
                self.check_event_direction()
                if self.check_position():
                    self.move()
                    self.check_food()
                else:
                    self.display_dead()

    def display(self, ):
        self.root.clear()
        self.root.place(self.food[0], self.food[1], self.root.FOOD)
        for pos in self.snake_pos:
            self.root.place(pos[0], pos[1], self.root.SNAKE)
        for pos in self.walls:
            self.root.place(pos[0], pos[1], self.root.WALL)
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

    def display_dead(self, ):
        self.root.clear()
        self.root.place_transparent(self.food[0], self.food[1], self.root.FOOD)
        for pos in self.snake_pos:
            self.root.place_transparent(pos[0], pos[1], self.root.SNAKE)
        for pos in self.walls:
            self.root.place_transparent(pos[0], pos[1], self.root.WALL)
        self.root.show()

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
            return self.running
        else:
            return self.running

    def check_food(self, ):
        if self.snake_pos[-1] == self.food:
            self.generate_food()
        else:
            self.snake_pos.pop(0)
