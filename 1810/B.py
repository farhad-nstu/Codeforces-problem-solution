t = int(input())
while t > 0:
    t -= 1
    
    n = int(input())
    
    res = []
    while n != 1:
        if n%2 == 0:
            res = []
            break
        
        if ((n+1)/2)%2 == 1:
            res.append(1)
            n = (n+1) / 2
        else:
            res.append(2)
            n = (n-1) / 2
    
    if not res or len(res) > 40:
        print(-1)
    else:
        print(len(res))
        print(" ".join(str(c) for c in res[::-1]))
            