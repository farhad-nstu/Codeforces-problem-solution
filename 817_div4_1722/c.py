t=int(input())
while t>0:
    t-=1
    n = int(input())

    a1 = list(map(str, input().split()))
    a2 = list(map(str, input().split()))
    a3 = list(map(str, input().split()))

    cache = {}
    tmp = {}
    c1, c2, c3 = 0, 0, 0
    for e in a1:
        cache[e] = 1
        tmp[e] = 1
        c1 += 3
    
    for e in a2:
        if e in cache:
            c1 -= 2
            c2 += 1
            cache[e] += 1
        else:
            cache[e] = 1
            tmp[e] = 2
            c2 += 3
    
    for e in a3:
        if e in cache:
            if cache[e] == 2:
                c1 -= 1
                c2 -= 1
            else:
                if e in tmp:
                    if tmp[e] == 1:
                        c1 -= 2
                    else:
                        c2 -= 2
                    c3 += 1
        else:
            c3 += 3

    print(c1, c2, c3)