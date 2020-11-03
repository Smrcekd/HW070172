# Numerology.py
# Value of the name based on the number
#by David Smrček


def main():
    name = input("Type your name: ")
    name = name.lower()
    x = 0
    for ch in name:
        x = int(ord(ch)) + x - 96
        
    print("The numeric value of your name is {0}.".format(x))

main()
