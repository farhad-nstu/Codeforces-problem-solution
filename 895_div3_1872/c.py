def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

t = int(input())
while t>0:
    t-=1
    l, r = map(int, input().split())

    status = False
    a, b = r-2, 2
    while l <= a + b <= r:
        if gcd(a, b) != 1:
            status = True
            break
        a -= 1
        b += 1
    
    if status:
        print(a, b)
    else:
        print(-1)
