t=int(input())
while t>0:
    t-=1
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    status = False
    for i in range(n):
        if a[i] == k:
            status = True
    if status:
        print("YES")
    else:
        print("NO")