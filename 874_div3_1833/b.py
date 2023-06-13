t=int(input())
while t>0:
    t-=1
    
    n,k = map(int,input().split())
    
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    a_pair = []
    for i in range(n):
        a_pair.append([a[i], i])
    
    a_pair.sort()
    b.sort()
        
    
    res = [0]*n
    for i in range(n):
        res[a_pair[i][1]] = b[i]

    print(" ".join(str(c) for c in res))
    
    
    # 1 3 5 3 9
    # 1 3 3 5 9
    # 2 5 11 2 4
    # 2 2 4 5 11