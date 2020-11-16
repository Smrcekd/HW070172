#GCD calculator

def main():
    m, n = eval(input("Enter 2 numbers for the formula: "))

    try:
        if m < n:
            y = n
            n = m
            m = y
            
        while m != 0:
            y = m
            m = n % m
            n = y
        print("The GCD is {}".format(n))

    except TypeError:
        print("The input must be numerical.")

main()
