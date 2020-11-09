# Algorith computing square roots
# by David Smrček

import math#Makes the math library available.
def nextGuess(guess, x):
        g = (guess + x / guess)/2
        return g
    
def main():
    x = eval(input("Enter the number: "))
    y = eval(input("How many times should Newton´s method be applied?: "))

    g = x/2

    for i in range (y):
        g = nextGuess(g, y)
                   
        
    print("Square root of the chosen number is:",g) 
    
main()
