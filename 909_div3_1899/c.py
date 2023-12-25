t=int(input())
while t>0:
    t-=1
    n = int(input())
    a = list(map(int, input().split()))

    _sum = a[0]
    res = a[0]
    for i in range(1, n):
        if _sum < 0:
            _sum = 0
        if (a[i]%2 == 0 and a[i-1]%2 != 0) or (a[i]%2 != 0 and a[i-1]%2 == 0):
            _sum += a[i]
        else:
            _sum = a[i]
        
        res = max(res, _sum)
    print(res)

    # sub_arrays = []
    # for i in range(n):
    #     tmp = [a[i]]
    #     sub_arrays.append(tmp.copy())
    #     for j in range(i+1, n):
    #         if (a[j]%2 == 0 and tmp[-1]%2 != 0) or (a[j]%2 != 0 and tmp[-1]%2 == 0):
    #             tmp.append(a[j])
    #             sub_arrays.append(tmp.copy())
    
    # print(max(sum(sub_arrays)))
    # res = -float("inf")
    # tm = ""
    # for sub_array in sub_arrays:
    #     if sum(sub_array) >= res:
    #         res = sum(sub_array)
    #         tm = sub_array
    #     # res = max(res, sum(sub_array))
    # print(tm)
    # print(res)