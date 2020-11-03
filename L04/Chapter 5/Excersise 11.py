# Chaos3.py
# Allows user to input two initial values and number of iterations  
#by David Smrček


def main():
    n = eval(input("How many numbers should I print?"))
    x = eval(input("Enter a number between 0 and 1: "))
    y = eval(input("Enter another number between 0 and 1: "))
    z = "input"
    print("{2:<8}{0:<13.2f}{1:<6.2f}".format(x,y,z))
    print("---------------------------")
    for i in range(n):
        x = 3.9 * x - 3.9 * x * x
        y = 3.9 * y - 3.9 * y * y
        print("{2:^3}{0:>12.5f}{1:>10.5f}".format(x, y, (i+1)))

main()
