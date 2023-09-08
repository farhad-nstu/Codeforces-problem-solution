t=int(input())
while t>0:
    t-=1

    n = int(input())
    a = list(map(int, input().split()))

    count = 0
    l, r = 0, n-1
    while r > l:
        if a[l] == 1 and a[r] == 0:
            a[r] = 1
            a[l] = 0
            count += 1
        elif a[l] != 1:
            l += 1
        elif a[r] != 0:
            r -= 1
        
    print(count)
    

