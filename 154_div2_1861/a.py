def isPrime(n):
    for i in range(2, 9):
        if n%i == 0:
            return False 
    return True 

t=int(input())
while t>0:
    t-=1
    
    s = input()
    
    res = -1
    while len(s) > 2:
        if isPrime(int(s)):
            res = int(s)
            break
        s = s[:len(s)-1]
    
    print(s)
    
    if isPrime(int(s)):
        print(int(s))
    else:
        print(res)
            
    
    