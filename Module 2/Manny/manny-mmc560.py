""" Assignment: Manny
    Created on 27 oct. 2020
    @author: Mark Melnic """

DONATION_REQUIREMENT = 50

while True:
    donation = float(input("Enter the amount you want to donate: "))
    if donation < DONATION_REQUIREMENT:
        pass
    else:
        break

print("Thank you for your contribution of %.2f euro." % donation)
