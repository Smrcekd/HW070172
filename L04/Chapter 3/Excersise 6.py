# Program calculates the cost of the order
# In Konditorei coffee shop
# by David Smrček

import math #Makes the math library available.

def main():
    x1, y1 = eval(input("Write the cordinates of the first place (two numbers separated by a comma): "))
    x2, y2 = eval(input("Write the cordinates of the second place (two numbers separated by a comma): "))
    root1 = y2 - y1
    root2 = x2 - x1
    slope = root1 / root2
                           
    print("The slope of a line is", slope)
    
main()
