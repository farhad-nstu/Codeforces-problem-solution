t=int(input())
while t>0:
    t-=1
    
    n=int(input())
    a = []
    for i in range(n):
        a.append(list(map(int, input().split())))
    
    res = 0
    for i in range(n):
        if a[i][0] > a[i][1]:
            res += 1
            
    print(res)