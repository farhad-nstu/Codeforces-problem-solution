t=int(input())
while t>0:
    t-=1

    s = input()
    if s.index('a') == 0 or s.index('b') == 1 or s.index('c') == 2:
        print("YES")
    else:
        print("NO")