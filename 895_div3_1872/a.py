t=int(input())
while t>0:
    t-=1

    a, b, c = map(int, input().split())

    if a >= b:
        large = a
        small = b
    else:
        large = b
        small = a

    res = 0
    while large > small:
        res += 1
        large -= c
        small += c

    print(res)