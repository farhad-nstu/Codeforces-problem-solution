t=int(input())
while t>0:
    t-=1
    n = int(input())

    a1 = list(map(str, input().split()))
    a2 = list(map(str, input().split()))
    a3 = list(map(str, input().split()))

    visited = set()
    c1, c2, c3 = 0, 0, 0
    for e in a1:
        if e in a2 and e in a3:
            visited.add(e)
            continue
        elif e in a2:
            c1 += 1
            c2 += 1
            # visited.add(e)
        elif e in a3:
            c1 += 1
            c3 += 1
            # a3.remove(e)
        else:
            c1 += 3

        visited.add(e)
    
    for e in a2:
        if e in visited:
            continue
        if e in a3:
            c2 += 1
            c3 += 1
            # a3.remove(e)
        else:
            c2 += 3
        
        visited.add(e)
    
    for e in a3:
        if e in visited:
            continue
        c3 += 3

    print(c1, c2, c3)