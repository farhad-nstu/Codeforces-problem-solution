t=int(input())
while t>0:
    t-=1

    n=int(input())
    a=list(map(int,input().split()))
    res = 0
    for i in range(1, n):
        if a[i] >= a[i-1]:
            continue
        tmp = a[i]
        a[i] = max(0, a[i-1])
        a[i-1] = tmp
        res += 1
    print(a)
    print(res)