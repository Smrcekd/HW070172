#removeDuplicates.py
def isin(myList, x):
    for i in myList:
        if i == x:
            return True

def removeDuplicates(myList):
    newList = []
    for i in myList:
        if not isin(newList, i):
            newList.append(i)
    return newList

def main():
    myList = [1,2,3,4,5,6,7,8,9,1,2,9]
    print("Remove Duplicate: ", removeDuplicates(myList))

if __name__ == '__main__': main()
