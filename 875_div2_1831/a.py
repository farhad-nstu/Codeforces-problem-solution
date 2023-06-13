t = int(input())
while t>0:
    t-=1
    n = int(input())
    a = list(map(int,input().split()))
    b = []

    for i in range(n):
        b.append(n-a[i]+1)

    print(" ".join(str(i) for i in b))