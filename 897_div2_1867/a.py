t=int(input())
while t>0:
    t-=1

    n = int(input())
    a = list(map(int, input().split()))
    res = []
    for i in range(n):
        res.append(a[i] - a[i-1])
    print(" ".join(str(i) for i in a))