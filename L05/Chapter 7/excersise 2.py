#Quizscore_to_grage2.py
#by David Smrček


def main():
    n = eval(input("Enter your number grade: "))
    if n == 5:
        print("A")
    elif n == 4:
        print("B")
    elif n == 3:
        print("C")
    elif n == 2:
        print("D")
    elif n == 1:
        print("F")
    elif n == 0:
        print("F")
    else:
        print("Not this time, mate. Write number between 0 and 5")
        
main()
