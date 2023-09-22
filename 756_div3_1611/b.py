t=int(input())
while t>0:
    t-=1
    a, b = map(int, input().split())
    print( min( min(a,b), (a+b)//4) )

