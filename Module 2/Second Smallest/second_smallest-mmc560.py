""" Assignment: second smallest
    Created on 27 oct. 2020
    @author: Mark Melnic """

nr_of_elements = int(input("Enter the number of elements: "))

print("Enter the numbers you want to find the second smallest from:\n", end="")
numbers = []
for i in range(nr_of_elements):
    numbers.append(int(input()))

min = numbers[0]
for item in numbers:
    if item < min:
        min = item

numbers.remove(min)

min = numbers[0]
for item in numbers:
    if item < min:
        min = item

print("The second smallest number is: %i" % min)
