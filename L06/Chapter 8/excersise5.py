#Prime value determinator

import math as m

def main():
    n = eval(input("Write a positive whole number: "))
    while (n < 1) or (n % 1 != 0):
        n = eval(input("Error, write a positive whole number: "))


    for i in range (int(m.sqrt(n))):
        i = 2
        if (n % (i)) != 0:
            i = i+1
            if i > m.sqrt(n):
                exit()
        else:
            break
    print("Your number is prime.")
main()
