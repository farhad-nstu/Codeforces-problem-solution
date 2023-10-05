t = int(input())
while t>0:
    t-=1
    n = int(input())
    a = list(map(int, input().split()))

    res = []
    for i in range(n):
        if not res:
            if a[0] == 1:
                res.append(2)
                continue
            else:
                res.append(1)
                continue
        
        tmp = res[-1] + 1
        if tmp != a[i]:
            res.append(tmp)
        else:
            res.append(tmp + 1)
    
    print(res[-1])
        


