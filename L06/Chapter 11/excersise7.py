#innerProd.py
  
def main():
    myList = [1,2,3,4,5,6,7,8,9]
    newList =[9,1,8,2,7,3,6,4,5]
    sum = 0
    for i in range(len(myList)):
        x = myList[i] * newList[i]
        sum = sum + x
    print(sum)
main()
