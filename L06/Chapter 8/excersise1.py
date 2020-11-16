# fibonacci upgraded
def main():
 import math as m

def main():
    n = eval(input("Which number of the Fibonnaci sequence would you like to see?: "))
    count = 0
    x = 1
    y = 0

    while count < n:
        count = count + 1
        result = x + y
        x = y
        y = result
    print("Your chosen number is", result)

main()
