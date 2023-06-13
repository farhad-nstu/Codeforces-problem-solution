t = int(input())
while t > 0:
    t -= 1
    
    n = int(input())
    if n <= 1:
        print(1)
        continue

    if n % 2:
        print(-1)
        continue
    
    arr = []
    for i in range(2, n+1, 2):
        print(i,i-1)
        # arr.append(i)
        # arr.append(i-1)
    
    # l, r = arr[0], arr[-1]
    # if not sum(arr) % (r-l+1):
    #     print(-1)
    #     continue
    
    # print(' '.join(str(x) for x in arr))
        
    