#Goldbach Conjucture
import math as m

def primeNum(n):
        x = m.sqrt(n)
        i = 2
        while i <= x:
            val = n % i
            if val == 0:
                return None
            else:
                i = i + 1
        return n

def main():
   
    x = eval(input("Write a positive whole number: "))
    while True:
        
        if x == 0:
            x = eval(input("Your number must be higher than 0: "))
        elif (x % 1 != 0):
            x = eval(input("Your number was not whole: "))
        elif (x < 1):
            x = eval(input("Your number was not positive: "))
        elif (x % 2 != 0):
            x = eval(input("Your number entered was not even: "))
        else:
            n = x
            break
    while n > 0:
            prime1 = primeNum(n)
            if prime1 != None:
                    prime2 = x - prime1
                    test = primeNum(prime2)
                    if test != None:
                        print("{0} + {1} = {2}".format(prime1, prime2, x))
            n = n - 1

main()
