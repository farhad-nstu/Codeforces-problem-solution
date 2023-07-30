t=int(input())
while t>0:
    t-=1
    
    n = int(input())
    a = list(map(int,input().split()))
    
    b = sorted(a)
    
    status = True
    for i in range(n):
        if b[i] % 2 and not a[i] % 2:
            status = False
    
    print("YES") if status else print("NO")