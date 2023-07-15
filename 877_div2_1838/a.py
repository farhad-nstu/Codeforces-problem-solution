t=int(input())
while t>0:
    t-=1
    
    n=int(input())
    a = list(map(int,input().split()))
    a.sort()
    
    if a[0] < 0:
        print(a[0])
    else:
        print(a[-1])