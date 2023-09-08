t=int(input())
while t>0:
    t-=1

    n = int(input())
    a = list(map(int, input().split()))
    sorted_a = sorted(a)

    res = []
    for i in a:
        if i == sorted_a[-1]:
            res.append(i - sorted_a[-2])
        else:
            res.append(i - sorted_a[-1])

    print(" ".join(str(i) for i in res))