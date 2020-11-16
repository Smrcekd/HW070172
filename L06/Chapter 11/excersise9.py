#Sieve of Eratosthenes
def sieve(list):
    newList = []

    while len(list) != 0:
        
        newList.append(list[0])
        
        try:
            for i in range(len(list)):
                if list[i] % list[0] == 0:
                    list.remove(list[i])
        except:
            newList
    return newList 

def main():
    n = eval(input("Input value of n: "))
    list = []
    for i in range(n-1):
        list.append(i+2)
    list = sieve(list)
    
    list.remove(2)
    list.remove(4)
    print(list)

main()
