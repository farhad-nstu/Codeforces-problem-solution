t=int(input()) 
while t>0:
    t-=1
    
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    
    res_arr = []
    _sum = 0
    for i in range(1, n):
        tmp = abs(a[i-1]-a[i])
        res_arr.append(tmp)
        _sum += tmp
    
    # now k-1 numbers large item will remove
    res_arr.sort(reverse=True)
    for i in range(k-1):
        _sum -= res_arr[i]
    print(_sum)