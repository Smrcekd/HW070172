# Program to find the the average of a series of numbers
# The amount of numbers and N is provided by user
# by David Smrček

import math#Makes the math library available.


def main():
    n = int(input("How many numbers are to be summed?: "))
    x = eval(input(": "))
    for i in range(2, n+1):
            y = eval(input(": "))
            x = float(x) + float(y)
            result = x / n
        
    print("The average of the n is: ", result) 
    
main()
