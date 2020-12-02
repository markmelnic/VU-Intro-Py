""" Assignment: Snake
    Created on 29 oct. 2020
    @author: Mark Melnic """

from ipy_lib3 import SnakeUserInterface

height = 32
width = 24

root = SnakeUserInterface(height, width)

init_pos = [(0,0), (1,0)]
food_pos = (0,0)

while True:
    root.clear()

    while food_pos in init_pos:
        food_pos = (root.random(height), root.random(width))
    root.place(root.random(height), root.random(width), 1)

    for pos in init_pos:
        root.place(pos[0], pos[1], 2)

    root.show()
    root.wait(500)

root.close()