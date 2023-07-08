from collections import Counter
t=int(input())
while t>0:
    t-=1
    
    n=int(input())
    a = list(map(int,input().split()))
    c = Counter(a)
    
    res = 0
    
    if sum(a) >= 0 and c[-1] % 2 == 0:
        print(res)
        continue
    
    for i in range(n):
        if a[i] == -1:
            a[i] = 1
            res += 1
            c = Counter(a)
            if sum(a) >= 0 and c[-1] % 2 == 0:
                break
        # elif a[i] == 1:
        #     a[i] = -1
        #     res += 1
        #     c = Counter(a)
        #     if sum(a) >= 0 and c[-1] % 2 == 0:
        #         break
    
    print(res)
            
            