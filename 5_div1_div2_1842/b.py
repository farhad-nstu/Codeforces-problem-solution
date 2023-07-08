t=int(input())
while t>0:
    t-=1
    
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    
    res = 0
    for e in a:
        if (e&x) + (e^x) == x:
            res |= e
        else:
            break
    
    for e in b:
        if (e&x) + (e^x) == x:
            res |= e
        else:
            break
    
    for e in c:
        if (e&x) + (e^x) == x:
            res |= e
        else:
            break
    
    if res == x:
        print("Yes")
    else:
        print("No")
        