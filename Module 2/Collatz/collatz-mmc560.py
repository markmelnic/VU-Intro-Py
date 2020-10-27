""" Assignment: collatz
    Created on 27 oct. 2020
    @author: Mark Melnic """

number = int(input("Enter a starting number: "))

print("The Collatz sequence for %i is: %i " % (number, number), end="")

sequence = [number]
while True:

    if number == 1:
        break

    if number % 2 == 0:
        number = int(number / 2)
    else:
        number = int(3 * number + 1)

    print(str(number) + " ", end="")
