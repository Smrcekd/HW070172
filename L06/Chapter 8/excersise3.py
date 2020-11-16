# Double the investment
def main():
    apr = eval(input("Enter the the annual interest rate? "))
    apr = .01*apr
    inv = eval(input("Enter the initial investment? "))

    i = inv
    interest = 0
    year = 0
    
    while inv > .5 * i:
        year = year+1
        interest = i * apr
        i = i + interest

    
    print("The initial investment will double in", year, "years")

main()
