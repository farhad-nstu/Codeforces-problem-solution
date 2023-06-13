t = int(input())
while t > 0:
    t -= 1
    n, k = map(int, input().split())
    
    if k == 0:
        for i in range(n):
            print(int(-1))
        continue
    
    x = 0
    for i in range(1, n+1):
        if (i * (i+1) / 2) <= k:
            x = i
        else:
            break
    
    lock_sum = x*(x+1)/2
    extra_sum = k - lock_sum
    for i in range(1, n+1):
        if i == x+1:
            if extra_sum == 0:
                print(int(-1000))
            else:
                val = -( ( (x - extra_sum + 1) * 2 ) - 1 )
                print(int(val))
        elif i <= x:
            print(int(2))
        elif i > x+1:
            print(int(-1000))
    