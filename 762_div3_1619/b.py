import math

t=int(input())
while t>0:
    t-=1

    n = int(input())
    res = 1
    set_ = set()

    i = 1
    while i*i <= n:
        set_.add(i*i)
        i += 1

    j = 1
    while j*j*j <= n:
        set_.add(j*j*j)
        j += 1

    print(len(set_))