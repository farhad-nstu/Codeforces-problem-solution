t=int(input())
while t>0:
    t-=1
    
    a = []
    for i in range(8):
        a.append(list(map(str,input())))

    res = ""
    column = 8
    for i in range(8):
        for j in range(8):
            if a[i][j] != ".":
                column = j
                break
        if a[i][j] != ".":    
            res += a[i][j]

    print(res)