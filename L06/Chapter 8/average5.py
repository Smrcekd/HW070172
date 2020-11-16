# average5.py

def main():
    fileName = input("What file are the numbers in? ")
    infile = open(fileName, 'r')
    total = 0.0
    count = 0
    xStr = input("Enter a number(<Enter> to quit) >> ")
    for line in infile:
        total = total + float(line)
        count = count + 1
    print("\The average of the number is", total / count)

main()
