t=int(input())
while t>0:
    t-=1

    n, m = map(int,input().split())

    a = []
    for i in range(n):
        a.append(input())

    if n<4 and m<4:
        print("NO")
        continue

    status = False
    for i in range(n):
        row_res = []
        for j in range(m):
            if a[i][j] not in row_res:
                row_res.append(a[i][j])

        if len(row_res) >= 4:
            status = True
            break

        col_res = []
        for k in range(i, -1, -1):
            if a[k][i] not in col_res:
                col_res.append(a[k][i])

        for k in range(i, n):
            if a[k][i] not in col_res:
                col_res.append(a[k][i])
        
        if len(col_res) >= 4:
            status = True
            break

    if status:
        print("YES")
    else:
        print("NO")