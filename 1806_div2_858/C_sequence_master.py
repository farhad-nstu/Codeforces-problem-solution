t=int(input())
while t>0:
    t-=1
    
    n = int(input())
    m = 2 * n 
    a = list(map(int, input().split()))
    
    res = 0
    for i in range(m):
        res += abs(a[i]) # initial add all value form 0 abs(distance) & [0 0 0 0] good array
    
    if m == 2:
        res = min(res, abs(a[1]-a[0])) # m==2 then just distance between them with result
        print(res)
        continue

    if m%4 == 0:
        tmp = 0
        for i in range(m):
            tmp += abs(a[i]-(-1)) # if m visible with 4 then use m-1 time -1 and just one m/2 [-1 -1 -1 m/2]
        for i in range(m):
            tmp -= abs(a[i]-(-1))
            tmp += abs(a[i]-(m//2)) # as fisrt add all compare with -1 so check which should be m/2 so that ans minmimum
            res = min(res, tmp)
            tmp -= abs(a[i]-(m//2))
            tmp += abs(a[i]-(-1))
    
    if m == 4:
        tmp = 0
        for i in range(m):
            tmp += abs(a[i]-2) # if m==4 add all distance from [2 2 2 2] good array
        res = min(res, tmp)
        print(res)
        continue
    
    print(res)
        