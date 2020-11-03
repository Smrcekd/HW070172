#change.py
#A program to calculate the value of some change in dollars
def main():
    print("Change Counter")
    print()
    print("Please enter the count of each coin type.")
    quarters = int(input("Quarters: "))
    dimes = int(input("Dimes: "))
    nickels = int(input("Nickels: "))
    pennies = int(input("Pennies: "))
    total = 0.25*quarters + 0.10*dimes + 0.05*nickels + 0.01*pennies
    print()
    print("The total value of your change is", total)

main()
                    
