t=int(input())
while t>0:
    t-=1
    
    n=int(input())
    a= list(map(int,input().split()))
    
    minDiff = float("inf")
    leftEl = a[0]
    rightEl = a[1]
    isSorted = True
    for i in range(1, n):
        if a[i] >= a[i-1]:
            diff = a[i] - a[i-1]
            if diff < minDiff:
                minDiff = diff
                leftEl = a[i-1]
                rightEl = a[i]
        else:
            isSorted = False
            break
    
    if not isSorted:
        print(0)
        continue
    
    opCount = (minDiff // 2) + 1
    # while leftEl <= rightEl:
    #     leftEl += 1
    #     rightEl -= 1
    #     opCount += 1
    print(opCount)