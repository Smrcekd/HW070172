# Program to calculate the volume and surface area of a sphere
# From its radius
# by David Smrček

import math #Makes the math library available.

def main():
    r = eval(input("Please enter a radius of the sphere: "))
    pi = 3.14159265359
    V = (4/3) * pi * (r**3)
    A = 4 * pi * (r**2)

    print("The volume of the sphere is", V)
    print("The surgace area of the sphere is", A)

main()
