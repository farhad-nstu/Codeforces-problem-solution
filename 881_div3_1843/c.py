t=int(input())
while t>0:
    t-=1
    
    n=int(input())
    
    res = 0
    while n:
        res += n
        n = n//2
    print(res)