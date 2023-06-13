t=int(input())
while t>0:
    t-=1
    
    n = int(input())
    a = list(map(int,input().split()))
    
    x = 0
    for el in a:
        x ^= el
    
    print(x)
        
    # xor all arr elements with this x
    for i in range(n):
        a[i] ^= x
        
    # for duplicate check
    y = 0 
    for i in range(n):
        y ^= a[i]
    
    if y == 0:
        print(x)
    else:
        print(-1)
        