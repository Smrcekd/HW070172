#futval.py
#A program to compute the value of investment
#carried 10 years into the future
#by David Smrček

def main():
    print("This program calculates the future value")
    print("of a 10-year investment")

    principal = eval(input("Enter the initial principal: "))
    apr = eval(input("Enter the annual interest rate: "))
    x = eval(input("Enter the number of years: "))
    print("{0:<} {1:>10}".format("Year", "Value"))
    print("----------------")

    for i in range (x):
        principal = principal * (1 + .01 * apr)

        print("{0:>2}      ${1:<}.{2:0^2}".format(i+1, int(principal), int(principal%1 * 100)))

main()

