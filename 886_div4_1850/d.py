t=int(input())
while t>0:
    t-=1
    
    n, k = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort()
    
    length = 0
    res = 0
    is_length_greater_than_1 = False
    for i in range(1, n):
        if length > 0:
            is_length_greater_than_1 = True
         
        if abs(a[i] - a[i-1]) <= k:
            length += 1
        else:
            res = max(res, length)
            length = 0
    
    res = max(res, length)
                    
    if res:
        res += 1
        print(n - res)
    else:
        if not is_length_greater_than_1:
            print(n-1)
        else:
            print(res)