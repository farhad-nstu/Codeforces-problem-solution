t = int(input())
while t > 0:
    t -= 1


    a,b,c,d = map(int, input().split())
    if ((a<c<b) or (a>c>b)) and ((a<d<b) or (a>d>b)):
        print("NO")
    elif (a<c<b) or (a>c>b) or (a<d<b) or (a>d>b):
        print("YES")
    else:
        print("NO")