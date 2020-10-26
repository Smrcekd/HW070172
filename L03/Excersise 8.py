#futval.py
#A program to compute the value of investment
#carried 10 years into the future

def main():
    print("This program calculates the future value")
    print("of a yearly investment")

    
    principal = eval(input("What is your fixed annual investment: "))
    rate = eval(input("Enter the yearly rate: "))
    periods = eval(input("Enter the number of compounding periods: "))
    
    for i in range(10*periods):
        principal = principal * (1 + rate/periods)

    print("The value in 10 years is", principal)

main()
