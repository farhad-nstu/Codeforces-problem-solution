t=int(input())
while t>0:
    t-=1

    n=int(input())
    a=list(map(int,input().split()))

    b = a.copy()
    for i in range(1, n):
        tmp = b[i]
        b[i] = b[i-1]
        b[i-1] = tmp
    
    # print(a, b)
    # break
    
    status = True
    for i in range(n):
        if a[i] == b[i]:
            status = False
            break

    if status:
        print("YES")
    else:
        print("NO")