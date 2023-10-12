t=int(input())
while t>0:
    t-=1

    n=int(input())
    a=list(map(int,input().split()))

    maxUnsortedValue = 0
    for i in range(1, n):
        if a[i] < a[i-1]:
            maxUnsortedValue = max(maxUnsortedValue, a[i-1])
    print(maxUnsortedValue)