t=int(input())
while t>0:
    t-=1
    
    n, k = map(int,input().split())
    a = list(map(int,input().split()))
    
    res = []
    maxEl = max(a)
    while maxEl > 0:
        
        indexOfMaxEl = a.index(maxEl)
        maxEl -= k
        if maxEl <= 0:
            res.append(indexOfMaxEl + 1)
            
        a[indexOfMaxEl] = maxEl
        
        maxEl = max(a)
    
    print(" ".join(str(e) for e in res))