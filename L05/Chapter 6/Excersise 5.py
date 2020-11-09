# Program to calculate the cost per square inch of a circular pizza
# Given its diameter and price
# by David Smrček

import math #Makes the math library available.
def pizzaArea(d):
    r = d/2
    A = math.pi * (r**2)
    return A

def pizzaCost(price, A):
    pizza = price / A
    return pizza

def main():
    d = eval(input("Please enter a diameter of the pizza: "))
    price = eval(input("Please enter the price of the pizza in euros: "))
    A = pizzaArea(d)
    pizza = pizzaCost(price, A)
                       
    print("The pizza has", A, "square inches")
    print("The cost per square inch of circular pizza is", pizza, "euros")

main()
