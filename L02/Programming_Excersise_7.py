# File: chaos.py
# A simple program illustrating chaotic behaviour

def main():
    print(  "This program illustrates a chaotic function")
    n = eval(input("How many numbers should I print?"))
    x1 = eval(input("Enter a number between 0 and 1: "))
    x2 = eval(input("Enter another number between 0 and 1: "))
    for i in range(n):
        x1 = 2.0 * x1 * (1 - x1)
        x2 = 2.0 * x2 * (1 - x2)
        print("       %.5f     %.5f" % (x1,x2))

main()
