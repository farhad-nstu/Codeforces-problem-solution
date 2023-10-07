t=int(input())
while t>0:
    t-=1

    n = int(input())
    a = list(map(int, input().split()))
    res_arr = [a[0]]
    for i in range(1, n):
        if a[i] < a[i-1]:
            res_arr.append(a[i])
        res_arr.append(a[i])
    
    print(len(res_arr))
    print(" ".join(str(e) for e in res_arr))