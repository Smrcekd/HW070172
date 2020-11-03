# Program to calculate the cost per square inch of a circular pizza
# Given its diameter and price
# by David Smrček

import math #Makes the math library available.

def main():
    d = eval(input("Please enter a diameter of the pizza: "))
    price = eval(input("Please enter the price of the pizza in euros: "))
    π = 3.14159265359
    r = d/2
    A = π * (r**2)
    pizza = price / A
                       
    print("The pizza has", A, "square inches")
    print("The cost per square inch of circular pizza is", pizza, "euros")

main()
