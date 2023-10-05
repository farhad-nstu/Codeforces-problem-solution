t=int(input())
while t>0:
    t-=1

    n = int(input())
    status = True
    maxSum = 0
    v1, v2 = 0, 0
    for _ in range(n):
        # a.append(list(map(int, input().split())))
        a, b = map(int, input().split())
        if not maxSum:
            maxSum = a + b
            v1, v2 = a, b
            continue

        if (a + b > maxSum and b > v2) or (a + b == maxSum and b == v2):
            status = False
    
    if not status:
        print(-1)
    else:
        if (v1 < 1) or (v1 > 10**9):
            print(-1)
        else:
            print(v1)
    