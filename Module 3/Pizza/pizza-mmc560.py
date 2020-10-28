""" Assignment: pizza
    Created on 28 oct. 2020
    @author: Mark Melnic """

M_INGREDIENTS = 10
M_USING = 3

L_INGREDIENTS = 9
L_USING = 4


def factorial(number: int) -> int:
    prod = 1
    for n in [number - i for i in range(number)]:
        prod *= n
    return prod


def possibilities(ingredients: int, used: int) -> int:
    return factorial(ingredients) / factorial(used) / factorial(ingredients - used)


mario_pizzas = possibilities(M_INGREDIENTS, M_USING)
luigi_pizzas = possibilities(L_INGREDIENTS, L_USING)

print("Mario can make %i pizzas" % mario_pizzas)
print("Luigi can make %i pizzas" % luigi_pizzas)

if mario_pizzas > luigi_pizzas:
    print("Mario has won the bet")
else:
    print("Luigi has won the bet")
