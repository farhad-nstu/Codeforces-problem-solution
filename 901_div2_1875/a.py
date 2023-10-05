t=int(input())
while t>0:
    t-=1

    a, b, n = map(int, input().split())
    arr = list(map(int, input().split()))

    res = 0
    i = 0
    while i < n:
        c = b
        while i<n and c<a:
            c += arr[i]
            i += 1
        
        if i != n:
            i -= 1
        
        res += min(max(0, c-1), a)
        b = max(0, c-a)
        i += 1
    
    print(res)
