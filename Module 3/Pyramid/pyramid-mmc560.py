""" Assignment: pyramid
    Created on 28 oct. 2020
    @author: Mark Melnic """

alphabet = "".join([chr(i) for i in range(ord("a"), ord("z") + 1)])
reversed_alphabet = alphabet[::-1]

for i in range(15):
    line = ""

    for j in range(int(80 - i * 2 / 2)):
        line += " "

    for j in range(i + 1):
        line += alphabet[j]

    for j in range(i):
        line += reversed_alphabet[len(alphabet) - (i - j)]

    for j in range(int(80 - i * 2 / 2)):
        line += " "

    print(line)
