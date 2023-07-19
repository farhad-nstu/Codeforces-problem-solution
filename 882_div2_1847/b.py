t=int(input()) 
while t>0:
    t-=1
    
    n = int(input())
    a = list(map(int, input().split()))
    
    res = 1
    for i in a:
        res &= i
        
    
    print(res)