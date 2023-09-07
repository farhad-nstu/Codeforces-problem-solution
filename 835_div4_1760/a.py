t=int(input())
while t>0:
    t-=1
    a = list(map(int, input().split()))
    a.sort()
    print(a[1])