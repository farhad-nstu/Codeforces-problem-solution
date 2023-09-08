t=int(input())
while t>0:
    t-=1
    a, b, c = map(int, input().split())

    # condition is as following
    # b - a = c - b
    # 2b = a + c
    # a = 2b - c1
    # c = 2b - a

    if ( (a + c) % (2*b) == 0 ) or ( (2*b - a) > 0 and (2*b - a) % c == 0 ) or ( (2*b - c) > 0 and (2*b - c) % a == 0 ):
        print("YES")
    else:
        print("NO")


