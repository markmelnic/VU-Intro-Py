""" Assignment: pyramid
    Created on 28 oct. 2020
    @author: Mark Melnic """

ROWS_NUMBER = 15
ROW_LENGTH = 80

alphabet = "".join([chr(i) for i in range(ord("a"), ord("z") + 1)])
reversed_alphabet = alphabet[::-1]

for i in range(ROWS_NUMBER):
    line = ""

    for j in range(int(ROW_LENGTH/2) - i):
        line += " "

    for j in range(i + 1):
        line += alphabet[j]

    for j in range(i):
        line += reversed_alphabet[len(alphabet) - abs(i - j)]

    for j in range(int(ROW_LENGTH/2) - i):
        line += " "

    print(line)
