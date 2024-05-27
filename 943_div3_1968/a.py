def gcd(a, b):
    if not b:
        return a
    return gcd(b, a%b)
    
t = int(input())
while t > 0:
    t -= 1
    n = int(input())
    max_val = -float("inf")
    res = 0
    for i in range(1, n):
        tmp = gcd(n, i) + i
        if tmp > max_val:
            max_val = tmp
            res = i
    print(res)