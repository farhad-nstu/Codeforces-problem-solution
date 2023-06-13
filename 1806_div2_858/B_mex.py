t=int(input())
while t>0:
    t-=1
    
    n = int(input())
    arr = list(map(int, input().split()))
    
    zeros, nonZeros = 0, 0
    res = 0
    for i in range(n):
        if arr[i] == 0:
            zeros += 1
        else:
            nonZeros += 1
    if not zeros or nonZeros >= zeros - 1:
        res = 0
    else:
        maxVal = max(arr)
        if maxVal == 1:
            res = 2
        else:
            res = 1
    print(res)