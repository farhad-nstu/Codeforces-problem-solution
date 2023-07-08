def calculateDifference(a,b):
    res = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            res += 1
    return res

t=int(input())
while t>0:
    t-=1
    
    n = int(input())
    S = input()
    T = input()
    
    res = 0
    diffBeforeRev = calculateDifference(S, T)
    if diffBeforeRev % 2 == 1:
        res = 2 * diffBeforeRev - 1
    else:
        res = 2 * diffBeforeRev
        
    # now bob reversed any of the string
    S = S[::-1]
    diffAfterRev = calculateDifference(S, T)
    if diffAfterRev == 0:
        res = min(res, 2)
    elif diffAfterRev % 2 == 0:
        res = min(res, 2 * diffAfterRev - 1)
    else:
        res = min(res, 2 * diffAfterRev)
    
    print(res)
        
    
    