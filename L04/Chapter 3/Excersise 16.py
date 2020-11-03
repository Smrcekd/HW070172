# Fibonacci sequence
# by David Smrček

import math#Makes the math library available.


def main():
    n = eval(input("Insert number from Fibbonaci sequence: "))
    x = 1
    result = 0
    for i in range (n+1):
        F = x + result
        x = result
        result = F
           
        
    print("The Fibonaccis sequence is:", i, ":", result) 
    
main()
