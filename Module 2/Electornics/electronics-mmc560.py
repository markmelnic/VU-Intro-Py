""" Assignment: electornics
    Created on 27 oct. 2020
    @author: Mark Melnic """

DISCOUNT_AMOUT = 15

items = []

for i in range(3):
    items.append(float(input("Enter the price of the item: ")))

max = items[0]
for item in items:
    if item > max:
        max = item

discount = max * DISCOUNT_AMOUT / 100
print("Discount: %.2f" % discount)

total = sum(items) - discount
print("Total: %.2f" % total)
