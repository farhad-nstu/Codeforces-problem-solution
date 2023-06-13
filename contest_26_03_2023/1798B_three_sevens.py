t = int(input())
while t > 0:
    t -= 1
    
    m = int(input())
    a = []
    for i in range(m):
        n = int(input())
        a.append(list(map(int, input().split())))
    
    s = set()
    res = [m]
    for i in range(m-1, -1, -1):
        tmp = a[i]
        for j in tmp:
            if j not in s:
                res[i] = j
            s.add(j)
        if res[i] == 0:
            print(-1, "\n")
    
    for i in res:
        print(i, " ")
    
    print("\n")
        