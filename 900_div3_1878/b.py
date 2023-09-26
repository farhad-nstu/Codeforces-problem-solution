t=int(input())
while t>0:
    t-=1
    n = int(input())

    a = []
    j = 1
    for i in range(n):
        a.append(j)
        j += 2
    print(" ".join(str(i) for i in a))
