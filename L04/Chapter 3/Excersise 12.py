# Program to find the sum of the cubes of the first n natural numbers
# N is provided by user
# by David Smrček

import math#Makes the math library available.

def main():
    n = eval(input("insert the n): "))
    fact = 1
    for x in range(n, 1, -1):
        fact = (fact + x**3)
        
    print("The sum of the n is", fact) 
    
main()
