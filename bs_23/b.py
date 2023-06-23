t=int(input())
while t>0:
    t -= 1
    
    n = int(input())
    a = list(map(int,input().split()))
    
    res = ""
    count = 0
    for i in range(1, n+1):
        if (a[i-1] - i) > 2:
            res = "Too chaotic"
            break
        
        if i != a[i-1]:
            if i < n:
                tmp = a[i]
                a[i] = a[i-1]
                a[i-1] = tmp
                if (a[i-1] - i) > 2:
                    res = "Too chaotic"
                    break
            count += 1
    # print(a)
    # break
    if res:
        print(res)
    else:
        print(count)