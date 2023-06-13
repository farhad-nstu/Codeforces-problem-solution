t = int(input())

while t > 0:
    n = int(input())
    s = input()
    res = n-1
    for i in range(1, n-1):
        if s[i-1] == s[i+1]:
            res -= 1
    print(res)
    t -= 1