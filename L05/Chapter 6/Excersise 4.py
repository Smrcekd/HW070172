# Program to find the sum of the n natural numbers
# N is provided by user
# by David Smrček

import math#Makes the math library available.
def sumN(n):
    fact = 1
    for x in range(n, 1, -1):
        fact = fact + x    
    return fact

def sumNCubes(n):
    fact2 = 1
    for x in range(n, 1, -1):
        fact2 = (fact2 + x**3)
    return fact2

def main():
    n = eval(input("insert the n): "))
    
    x = sumN(n)
    y = sumNCubes(n)
    
    print("The sum of the n is", x)     
    print("The sum of cubes is", y) 
    
main()
