""" Assignment: palindrome 1
    Created on 28 oct. 2020
    @author: Mark Melnic """

alphabet = "".join([chr(i) for i in range(ord("a"), ord("z"))])
print(alphabet + "z" + alphabet[::-1])
