# Program to determine the lenght of a ladder
# Required to a house.
# by David Smrček

import math#Makes the math library available.

def main():
    height = eval(input("How high is the ladder when leaned against the house (in meters): "))
    angle = eval(input("Under which angle is it leaned against the house: "))
    
    lenght = height/ math.sin(angle)

    print("The lenght of the ladder is", lenght,"meters") 
    
main()
