from collections import Counter
t=int(input())
while t>0:
    t-=1
    
    n=int(input())
    a = list(map(int,input().split()))
    max_val = 0
    c = {}
    for i in range(n):
        max_val = max(max_val, a[i])
        if a[i] not in c:
            c[a[i]] = 1
        else: 
            c[a[i]] += 1
    
    status = False
    max_val = max(a) 
    for i in range(1,max_val+1):
        if c[i-1] < c[i]:
            status = True
            print("NO")
            break

    if not status:
        print("YES")
            
            