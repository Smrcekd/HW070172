#Prime value determinator2

import math as m

def primeVal(n):

        x = m.sqrt(n)
        i = 2

        while i <= x:
            val = n % i
            if val == 0:
                return
            else:
                i = i + 1
        print(n)

def main():
    x = eval(input("Write a positive whole number: "))
    if x == 0:
        x = eval(input("Your number must be higher than 0: "))
    elif (x % 1 != 0):
        x = eval(input("Your number was not whole: "))
    elif (x < 1):
        x = eval(input("Your number was not positive: "))
    else:
        for n in range(x):
            primeVal(n+1)

main()
