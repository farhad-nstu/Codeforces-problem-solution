t=int(input())
while t>0:
    t-=1

    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    maxVal = max(a)
    if maxVal:
        print("YES")
    else:
        print("NO")