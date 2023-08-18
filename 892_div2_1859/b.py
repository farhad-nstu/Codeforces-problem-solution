t=int(input())
while t>0:
    t-=1

    n = int(input())
    res_arr = []
    minval = float("inf")
    r = 0
    
    for i in range(n):
        tmp = int(input())
        t_arr = list(map(int,input().split()))
        t_arr.sort()

        if tmp == 1:
            r += t_arr[0]
        else:
            k = t_arr[0]
            minval = min(minval, k)
            res_arr.append(t_arr[1])
    
    r += minval

    for i in range(1, len(res_arr)):
        r += res_arr[i]
    
    print(r)
    
