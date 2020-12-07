""" Assignment: Snake
    Created on 2 dec. 2020
    @author: Mark Melnic """

from ipy_lib3 import SnakeUserInterface

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

def generate_food():
    food_pos = (root.random(WIDTH), root.random(HEIGHT))
    while food_pos in snake_pos or food_pos in walls:
        food_pos = (root.random(WIDTH), root.random(HEIGHT))
    return food_pos

def display():
    root.clear()
    root.place(food_pos[0], food_pos[1], 1)
    for pos in snake_pos:
        root.place(pos[0], pos[1], 2)
    for pos in walls:
        root.place(pos[0], pos[1], 3)
    root.show()

def check_event_direction():
    new_piece = ()
    if event_data == "r":
        new_piece = (snake_pos[-1][0] + 1, snake_pos[-1][1])
    elif event_data == "l":
        new_piece = (snake_pos[-1][0] - 1, snake_pos[-1][1])
    elif event_data == "u":
        new_piece = (snake_pos[-1][0], snake_pos[-1][1] - 1)
    elif event_data == "d":
        new_piece = (snake_pos[-1][0], snake_pos[-1][1] + 1)
    return new_piece

if __name__ == "__main__":
    event_name = "arrow"
    snake_pos, event_data, walls = read_level()
    food_pos = snake_pos[0]

    root = SnakeUserInterface(WIDTH, HEIGHT)
    root.set_animation_speed(4)
    food_pos = generate_food()
    while True:
        display()

        ev = root.get_event()
        if ev.name == "arrow" and (
            (event_data == "r" and not ev.data == "l") or
            (event_data == "l" and not ev.data == "r") or
            (event_data == "u" and not ev.data == "d") or
            (event_data == "d" and not ev.data == "u")
        ):
            event_name = ev.name
            event_data = ev.data
            root.clear_text()

        if ev.data == "refresh":
            snake_pos.append(check_event_direction())
            if len(snake_pos) != len(set(snake_pos)) or any(pos in walls for pos in snake_pos):
                root.clear_text()
                root.print_("Game over")
                break
            else:
                for i, piece in enumerate(snake_pos):
                    piece = list(piece)
                    if piece[0] == -1:
                        piece[0] = WIDTH - 1
                        snake_pos[i] = tuple(piece)
                    elif piece[0] == WIDTH:
                        piece[0] = 0
                        snake_pos[i] = tuple(piece)
                    if piece[1] == -1:
                        piece[1] = HEIGHT - 1
                        snake_pos[i] = tuple(piece)
                    elif piece[1] == HEIGHT:
                        piece[1] = 0
                        snake_pos[i] = tuple(piece)

                if snake_pos[-1] == food_pos:
                    food_pos = generate_food()
                else:
                    snake_pos.pop(0)

    root.stay_open()
    root.close()
