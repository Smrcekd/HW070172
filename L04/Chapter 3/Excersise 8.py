# The Gregorian epact
# The value is used to figure out the date of Easter
# by David Smrček

import math #Makes the math library available.

def main():
    Y = int(input("Write a number of the year to figure out the date of Easter (4 digits): "))
    C = Y // 100
    epact = (8+(C//4) - C + ((8*C + 13)//25) + 11*(Y%19))%30
        
                           
    print("The value of the epact is", epact)
    
main()
