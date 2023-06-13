t = int(input())
while t > 0:
    x, y = map(int, input().split())
    x, y = abs(x), abs(y)
    res = x+y
    diff = abs(x-y)
    res += max(0, diff-1)
    print(res)
    t -= 1