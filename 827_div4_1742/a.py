t=int(input())
while t>0:
    t-=1

    a, b, c = map(int, input().split())

    if a+b == c or a+c == b or b+c == a:
        print("YES")
    else:
        print("NO")