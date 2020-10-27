""" Assignment: Manny
    Created on 27 oct. 2020
    @author: Mark Melnic """

while True:
    donation = float(input("Enter the amount you want to donate: "))
    if donation < 50:
        pass
    else:
        break

print("Thank you for your contribution of %.2f euro." % donation)
