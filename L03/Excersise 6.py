#futval.py
#A program to compute the value of investment
#carried 10 years into the future

def main():
    print("This program calculates the future value")
    print("of a 10-year investment")

    principal = eval(input("Enter the initial principal: "))
    apr = eval(input("Enter the annual interest rate: "))
    x = eval(input("Enter the number of years: "))
    for i in range(x):
        principal = principal * (1 + apr)

    print("The value in", x ,"year(s) is" , principal)

main()
