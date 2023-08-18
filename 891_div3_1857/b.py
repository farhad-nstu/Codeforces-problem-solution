t=int(input())
while t>0:
    t-=1

    n = int(input())
    a = list(map(int,input().split()))

    tmp = 0
    curr = float("inf")
    res = []
    while tmp < n-1:
        if tmp < len(a):
            maxVal = max(curr, a[tmp])
            res.append(maxVal)
        tmp += 1
        if tmp == n-2:
            n += 1
    
    print(res)