# Program determines the distance between two points
# Written by the user
# by David Smrček

import math #Makes the math library available.

def main():
    x1, y1 = eval(input("Write the cordinates of the first place (two numbers separated by a comma) in cm: "))
    x2, y2 = eval(input("Write the cordinates of the second place (two numbers separated by a comma) in cm: "))
    root1 = (x2 - x1)**2
   
    root2 = (y2 - y1)**2

    rootC = root1 + root2
    
    discRoot = math.sqrt(rootC)
                           
    print("The distance between the points", discRoot, "cm")
    
main()
