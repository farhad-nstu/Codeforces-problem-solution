t = int(input())
while t > 0:
    t -= 1

    a,b,c = map(int, input().split())

    if a<b<c:
        print("STAIR")
    elif a<b>c:
        print("PEAK")
    else:
        print("NONE")