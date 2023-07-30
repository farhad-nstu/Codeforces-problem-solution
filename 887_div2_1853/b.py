t=int(input())
while t>0:
    t-=1
    
    n, k = map(int,input().split())
    
    if k >= 30:
        print(0)
        continue
    
    countValidSeq = 0
    for i in range(n+1):
        isValidSeq = True 
        last = n
        prev = i
        for j in range(k-2):
            tmp = last - prev
            last = prev
            prev = tmp
            if prev <= last and prev > -1:
                continue
            else:
                isValidSeq = False
                break
            
        if isValidSeq:
            countValidSeq += 1
    
    print(countValidSeq)