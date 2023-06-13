t = int(input())
while t > 0:
    t -= 1
    
    inp1 = list(map(int, input().split()))
    n, k = inp1[0], inp1[1]
    
    arr = []
    for i in range(n):
        arr.append(list(map(int, input().split())))
        
    count = 0
    for i in range(n):
        for j in range(n):
            if arr[i][j] != arr[n-1-i][n-1-j]: # arr[0][0] will be arr[3][3] after 180 rotation 
                count += 1
    
    count //= 2
    if count > k:
        print("NO")
    else:
        if n%2 or not (k-count)%2:
            print("YES")
        else:
            print("NO")