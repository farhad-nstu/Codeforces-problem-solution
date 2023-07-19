t=int(input()) 
while t>0:
    t-=1
    
    n = int(input())
    s = input()
    
    if 'R' not in s or 'L' not in s: # if all L or all R then -1
        print(-1)
        continue
    
    res = 0
    for i in range(n):
        if i < n-1 and s[i] == 'L' and s[i+1] == 'R': # if we found any combination of LR then just print L th poistion
            res = i+1 # we work in 0 index based
            break
    print(res)
