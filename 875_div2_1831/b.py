t = int(input())
while t>0:
    t-=1
    n = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    
    s = set()
    map1, map2 = {}, {}
    c1 = 1
    for i in range(1,n):
        s.add(a[i-1])
        if a[i-1] == a[i]:
            c1 += 1
        else:
            if a[i-1] not in map1:
                map1[a[i-1]] = c1
            else:
                map1[a[i-1]] = max(map1[a[i-1]], c1)
            c1 = 1
    if a[n-1] not in map1:
        map1[a[n-1]] = c1
    else:
        map1[a[n-1]] = max(map1[a[n-1]], c1)
    s.add(a[n-1])
    
    c2 = 1
    for i in range(1,n):
        s.add(b[i-1])
        if b[i-1] == b[i]:
            c2 += 1
        else:
            if b[i-1] not in map2:
                map2[b[i-1]] = c2
            else:
                map2[b[i-1]] = max(map2[b[i-1]], c2)
            c2 = 1
    if b[n-1] not in map2:
        map2[b[n-1]] = c2
    else:
        map2[b[n-1]] = max(map2[b[n-1]], c2)
    s.add(b[n-1])
    
    res = 0
    for c in s:
        if c in map1 and c in map2:
            _sum = map1[c] + map2[c]
        elif c in map1:
            _sum = map1[c]
        else:
            _sum = map2[c]
        res = max(res, _sum)
        
    print(res)