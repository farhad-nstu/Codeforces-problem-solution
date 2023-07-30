t=int(input())
while t>0:
    t-=1
    
    n, m, k, h = map(int,input().split())
    a = list(map(int,input().split()))

    # print(n,m,k,h)
    res = 0
    for i in range(n):
        if a[i] + h >= m * k:
            res += 1
    print(res)