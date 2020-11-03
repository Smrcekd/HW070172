# Program to find the sum of the cubes of the first n natural numbers
# N is provided by user
# by David Smrček

import math#Makes the math library available.


def main():
    n = int(input("How many numbers are to be summed?: "))
    x = eval(input(": "))
    for i in range(2, n+1):
            y = eval(input(": "))
            x = x + y
            
        
    print("The sum of the n is: ", x) 
    
main()
