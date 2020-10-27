""" Assignment: Othello 1
    Created on 27 oct. 2020
    @author: Mark Melnic """

TOTAL_SQUARES = 64

white_pieces = int(input("Enter the number of white pieces on the board: "))
black_pieces = int(input("Enter the number of black pieces on the board: "))

total_pieces = white_pieces + black_pieces

print("The percentage of black pieces on the board is:", black_pieces*100/TOTAL_SQUARES)
print("The percentage of black pieces of all the pieces on the board is:", black_pieces*100/total_pieces)
