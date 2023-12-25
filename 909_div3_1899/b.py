t=int(input())
while t>0:
    t-=1
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()

    print(a)
    print(a[-1] - a[0])