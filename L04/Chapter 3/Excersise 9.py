# Program calculates the area of triangle
# Given the lenghts of its three sides
# by David Smrček

import math #Makes the math library available.

def main():
    a, b, c = eval(input("Write the lenghts of side a, b and c (respectively): "))
    s = (a + b + c)/ 2
    calculation = s*(s-a)*(s-b)*(s-c)

    A = math.sqrt(calculation)
    
        
                           
    print("The area of the triangle is", A, "cm2")
    
main()
