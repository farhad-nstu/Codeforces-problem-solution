t=int(input())
while t>0:
    t-=1
    
    n = int(input())
    a = list(map(int,input().split()))
    
    inPosition = 0
    for i in range(n):
        if a[i] == i+1:
            inPosition += 1
    
    if not inPosition:
        print(inPosition)
        continue
    
    if inPosition%2 == 0:
        inPosition = inPosition//2
    else:
        inPosition = (inPosition//2) + 1
        
    print(inPosition)