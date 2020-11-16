#Sieve of Eratosthenes
def Sieve(n): 
    prime = [True for i in range(n + 1)] 
    p = 2
    while (p * p <= n):  
        if (prime[p] == True):  
            for i in range(p * 2, n + 1, p): 
                prime[i] = False
        p += 1
    prime[0]= False
    prime[1]= False 
    for p in range(n + 1): 
        if prime[p]: 
            print(p)  
if __name__=='__main__':
    n = int(input("Enter the N >> "))
    
    list = Sieve(n)

    
# Code does not work, I am not sure why
#list.remove(2)
#I cannot find the way to not print 2s
