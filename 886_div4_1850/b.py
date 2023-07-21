t=int(input())
while t>0:
    t-=1
    
    n = int(input())
    a = []
    for i in range(n):
        a.append(list(map(int,input().split())))

    maxQuality = -float("inf")
    res = 1
    for i in range(n):
        if a[i][0] <= 10 and a[i][1] > maxQuality:
            maxQuality = a[i][1]
            res = i + 1

    print(res)