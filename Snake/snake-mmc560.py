""" Assignment: Snake
    Created on 2 dec. 2020
    @author: Mark Melnic """

from ipy_lib3 import SnakeUserInterface

HEIGHT = 32
WIDTH = 24
snake_pos = [(0, 0), (1, 0)]
food_pos = (0, 0)
event_name = "arrow"
event_data = "r"

if __name__ == "__main__":
    root = SnakeUserInterface(WIDTH, HEIGHT)
    while food_pos in snake_pos:
        food_pos = (root.random(WIDTH), root.random(HEIGHT))

    while True:
        ev = root.get_event()
        if ev.name == "arrow":
            if (
                (event_data == "r" and not ev.data == "l")
                or (event_data == "l" and not ev.data == "r")
                or (event_data == "u" and not ev.data == "d")
                or (event_data == "d" and not ev.data == "u")
            ):
                event_name = ev.name
                event_data = ev.data

        if event_name == "arrow":
            if event_data == "r":
                new_piece = (snake_pos[-1][0] + 1, snake_pos[-1][1])
            elif event_data == "l":
                new_piece = (snake_pos[-1][0] - 1, snake_pos[-1][1])
            elif event_data == "u":
                new_piece = (snake_pos[-1][0], snake_pos[-1][1] - 1)
            elif event_data == "d":
                new_piece = (snake_pos[-1][0], snake_pos[-1][1] + 1)

            if new_piece in snake_pos:
                root.print_("Game over")
                break
            else:
                snake_pos.append(new_piece)
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
                    while food_pos in snake_pos:
                        food_pos = (root.random(WIDTH), root.random(HEIGHT))
                else:
                    snake_pos.pop(0)

        root.clear()
        root.place(food_pos[0], food_pos[1], 1)
        for pos in snake_pos:
            root.place(pos[0], pos[1], 2)
        root.show()
        # root.wait(500)

    root.stay_open()
    root.close()
