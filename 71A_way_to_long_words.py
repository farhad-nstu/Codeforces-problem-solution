n = int(input())
while n > 0:
    s = input()
    if len(s) > 10:
        res = s[0]
        ln = len(s[0:len(s)-2])
        res += str(ln) + s[len(s)-1]
        print(res)
    else:
        print(s)
    n -= 1