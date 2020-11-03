# Program to determine the distance to a lighting strike
# Based on the time elapsed between the flash and sound of thunder
# by David Smrček

import math #Makes the math library available.

def main():
    s = eval(input("What time elapsed between the flash and the sound of thunder: "))
    result = (5280 / 1100) * s
                           
    print("The distance to a lightning strike is", result, "miles")
    
main()
