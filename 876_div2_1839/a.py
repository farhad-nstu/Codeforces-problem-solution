t=int(input())
while t>0:
    t-=1
    
    n, k = map(int, input().split())
    
    if k == 1:
        res = n
    else:
        res = n//k + 1
        if n%k > 1:
            res += 1
            
    print(res)