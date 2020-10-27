""" Assignment: plumber
    Created on 27 oct. 2020
    @author: Mark Melnic """

CALL_OUT_COST = 16

hourly_wage = float(input("Enter the hourly wages: "))

hours_worked = float(input("Enter the number of hours worked: "))

if hours_worked - int(hours_worked) >= 0.5:
    hours_worked = int(hours_worked) + 1

total_cost = hours_worked * hourly_wage + CALL_OUT_COST

print("The total cost of this repair is: %.2f euro." % total_cost)
