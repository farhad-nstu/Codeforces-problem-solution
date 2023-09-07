t=int(input())
while t>0:
    t-=1

    n, s, r = map(int, input().split())
    maxVal = s - r
    a = [maxVal]
    n = n-1

    modulas = r % n
    div = r // n
    tmp = [div] * n
    a += tmp

    if modulas != 0:
        for i in range(1, modulas + 1):
            a[i] += 1
    
    print(" ".join(str(x) for x in a))
        