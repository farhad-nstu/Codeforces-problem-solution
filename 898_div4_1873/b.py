t=int(input())
while t>0:
    t-=1

    n = int(input())
    a = list(map(int, input().split()))
    minVal = min(a)
    a[a.index(minVal)] = minVal + 1

    res = 1
    for i in a:
        res *= i
    print(res)