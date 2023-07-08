t=int(input())
while t>0:
    t-=1

    L, R = map(str,input().split())
    
    if len(L) > len(R):
        while len(L) > len(R):
            R = "0" + R
    elif len(L) < len(R):
        while len(L) < len(R):
            L = "0" + L
    
    # we take the absolute difference of two digits until they are matched. If not matched then take 9
    res = 0
    is_matched = True
    for i in range(len(L)):
        if not is_matched:
            res += 9
            continue
        
        if L[i] != R[i]:
            is_matched = False
            res += abs(int(L[i]) - int(R[i]))
    
    print(res)
            
            