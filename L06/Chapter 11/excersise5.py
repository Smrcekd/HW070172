#operations.py
def count(myList, x):
    tot = 0
    for i in myList:
        if i == x:
            tot = tot + 1
    return tot


def isin(myList, x):
    for i in myList:
        if i == x:
            return True


def index(myList, x):
    for i in range (len(myList)):
        if myList[i] == x:
            return i
            break


def reverse(myList):
    newList = []
    for i in range(len(myList)):
        x = myList[-1 * (i + 1)]
        newList.append(x)
    return newList


def sort(myList):
    newList = []
    for i in range (len(myList)):
        x = min(myList)
        newList.append(x)
        myList.remove(x)
    return newList

        


def main():
    myList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    myList = myList * 2
    x = 2
    print("Count of x: ", count(myList, x))
    print("X in myList: ", isin(myList, x))
    print("Index of x: ", index(myList, x))
    print("Reverse list: ", reverse(myList))
    print("Sort List: ", sort(myList))
if __name__ == '__main__': main()
