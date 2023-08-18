t=int(input())
while t>0:
    t-=1
    
    n = int(input())
    s = input()
    
    prefix = [0] * n
    a = set()
    i = 0
    while i < n:
        a.add(s[i])
        prefix[i] = len(a)
        i += 1
     
    suffix = [0] * n    
    a.clear()
    i = n-1
    while i > -1:
        a.add(s[i])
        suffix[i] = len(a)
        i -= 1
    
    res = 0
    for i in range(n-1):
        res = max(res, prefix[i] + suffix[i+1])
    
    print(res)