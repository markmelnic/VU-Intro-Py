""" Assignment: palindrome 2
    Created on 28 oct. 2020
    @author: Mark Melnic """

alphabet = "".join([chr(i) for i in range(ord("a"), ord("z") + 1)])

letter = input("Enter a letter: ")

new_alphabet = alphabet[: alphabet.find(letter)]

print(new_alphabet + letter + new_alphabet[::-1])
