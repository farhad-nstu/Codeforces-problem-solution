import re
t=int(input())
while t>0:
    t-=1
    
    n = int(input())
    a = list(map(int,input().split()))
    s = input()
    
    cache = {}
    for i in range(n):
        if isinstance(a[i], int):
            if a[i] in cache:
                a[i] = cache[a[i]]
            else:
                cache[a[i]] = s[i]
                a[i] = s[i]
    
    new_str = "".join(c for c in a)
    if new_str == s:
        print("YES")
    else:
        print("NO")