# Program calculates the cost of the order
# In Konditorei coffee shop
# by David Smrček

import math #Makes the math library available.

def main():
    c = eval(input("How many pounds of coffee did you order: "))
    price = (c*10.50) + (c*0.86) + 1.50
                           
    print("The cost of the order is", price, "dollars")
    
main()
