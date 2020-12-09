""" Assignment: Snake
    Created on 2 dec. 2020
    @author: Mark Melnic """

from Snake.logic import Logic

DEFAULT_SNAKE_POS = [(0, 0), (1, 0)]
DEFAULT_EVENT_DATA = "r"

def read_level(filename):
    walls = []
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
        snake_pos = DEFAULT_SNAKE_POS
        event_data = DEFAULT_EVENT_DATA
    return snake_pos, event_data, walls

if __name__ == "__main__":
    filename = str(input("Do you have a level to load? Type the file name here, otherwise just press ENTER: "))
    snake_game = Logic(read_level(filename))
