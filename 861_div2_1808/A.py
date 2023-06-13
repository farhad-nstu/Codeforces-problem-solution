t=int(input())
while t>0:
    t-=1
    
    inp = list(map(int, input().split()))
    l, r = inp[0], inp[1]
    
    maxVal, res = -1, 0
    for i in range(l, r+1):
        s = str(i) # there will TLE if convert it to array instead string
        s = sorted(s)
        curr = int(s[len(s)-1]) - int(s[0])
        if curr >= maxVal:
            maxVal = curr
            res = i
        if maxVal == 9:
            break
    print(res)
        
        