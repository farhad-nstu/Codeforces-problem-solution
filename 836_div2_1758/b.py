t=int(input())
while t>0:
    t -= 1
    
    n=int(input())
    
    if n%2:
        res = [1] * n # if odd just print 1 n times
    else:
        res = [2] * (n-2) # if even print 2 (n-2) times and then 1 and 3
        res += [1, 3]
    
    print(" ".join(str(i) for i in res))