# Program to calculate the volume and surface area of a sphere
# From its radius
# by David Smrček

import math #Makes the math library available.
def sphereArea(r):
    area = 4 * math.pi * (r**2)
    return area
def sphereVolume(r):
    volume = (4/3) * math.pi * (r**3)
    return volume

def main():
    r = eval(input("Please enter a radius of the sphere: "))
    a = sphereArea(r)
    v = sphereVolume(r)
    print("The volume of the sphere is", a)
    print("The surgace area of the sphere is", v)

main()
