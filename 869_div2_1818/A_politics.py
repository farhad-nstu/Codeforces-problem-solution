t = int(input())
while t > 0:
    t -= 1
    
    tmp = list(map(int, input().split()))
    n,k = tmp[0], tmp[1]
    
    arr = []
    for i in range(n):
        arr.append(input())
    
    res = 1
    for i in range(1, n):
        if arr[i] == arr[0]:
            res += 1
    
    print(res)