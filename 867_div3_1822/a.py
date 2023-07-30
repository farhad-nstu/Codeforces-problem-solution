m=int(input())
while m>0:
    m-=1
    
    n, t = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    
    i = 0
    maxEntertain = -float("inf")
    maxIdx = 0
    
    while i < n:
        if b[i] > maxEntertain and t >= a[i]:
            maxEntertain = b[i]
            maxIdx = i + 1
        i += 1
        t -= 1
        
    if not maxIdx:
        print(-1)
    else:
        print(maxIdx)