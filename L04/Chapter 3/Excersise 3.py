# Program to compute the molecular weight of carbohydrategrams/mole
# from hydrogen, carbon and oxygen atoms in the molecule
# by David Smrček

import math #Makes the math library available.

def main():
    h = int(input("Write the number of hydrogen atoms: "))
    c = int(input("Write the number of carbon atoms: "))
    o = int(input("Write the number of oxygen atoms: "))

    H = h * 1.00794
    C = c * 12.0107
    O = o * 15.9994

    R = H + C + O
                           
    print("The molecular weight of this carbohydrate is", R, "gram / mole")

main()
