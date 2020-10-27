""" Assignment: vat
    Created on 27 oct. 2020
    @author: Mark Melnic """

price = float(input("Enter the price of an article including VAT: "))

without_vat = price * 79 / 100

print("This article will cost " + str(without_vat) + r" euro without 21.00% VAT.")
