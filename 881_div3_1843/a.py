t=int(input())
while t>0:
    t-=1
    
    n=int(input())
    a=list(map(int,input().split()))
    
    res = 0
    while a:
        maxVal = max(a)
        minVal = min(a)
        res += maxVal - minVal
        a.remove(maxVal)
        if a:
            a.remove(minVal)
    
    print(res)