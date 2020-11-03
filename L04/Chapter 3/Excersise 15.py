# Program approximates the value of pi
# By summing the terms of series
# by David Smrček

import math#Makes the math library available.


def main():
    n = eval(input("Number of terms for the sum: "))
    x = 0
    m = 1
    for i in range (1,2 * n + 1, 2):
        x = x + (m *4/i)
        m = -m
    result = math.pi - x
    
        
    print("The approximate value of pi is: ", result) 
    
main()
