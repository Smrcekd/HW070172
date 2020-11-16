#shuffle.py
from random import random

def shuffle(myList):
    newList = []
    for i in range (len(myList)):
        x = int(random() * len(myList)) - 1
        newList.append(myList[x])
        myList.remove(myList[x])
    return newList

def main():
    myList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    myList = myList
    print("Shuffle List: ", shuffle(myList))

if __name__ == '__main__': main()
