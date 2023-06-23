t=int(input())
while t>0:
    t-=1
    
    n=int(input())
    a=list(map(int,input().split()))
    
    sum_ = 0
    opr = 0
    status = 0
    
    for i in range(n):
        sum_ += abs(a[i])
        
        if not a[i]:
            continue
        
        if a[i] < 0:
            status = 1
        else:
            if status:
                opr += 1
            status = 0
            
    if status:
        opr += 1
    
    print(str(sum_) + " " + str(opr))
