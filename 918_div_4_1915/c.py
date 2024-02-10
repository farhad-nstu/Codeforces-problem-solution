import math
t = int(input())
while t > 0:
    t -= 1

    n = int(input())
    a = list(map(int, input().split()))
    _sum = sum(a)
    sqrt_val = math.sqrt(_sum)
    if sqrt_val == int(sqrt_val):
        print("YES")
    else:
        print("NO")