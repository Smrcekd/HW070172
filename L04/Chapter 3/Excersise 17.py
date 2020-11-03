# Algorith computing square roots
# by David Smrček

import math#Makes the math library available.


def main():
    x = eval(input("Enter the number: "))
    y = eval(input("How many times should Newton´s method be applied?: "))

    g = x/2

    for i in range (y):
        g = (g + x / g)/2
        result = g - (math.sqrt(x))
                   
        
    print("Square root of the chosen number is:",g ,":", result) 
    
main()
