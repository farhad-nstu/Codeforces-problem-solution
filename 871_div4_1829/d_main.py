# def isValid(n,m):
#     if n==m:
#         return True
#     if n%3:
#         return False
#     return isValid((2*n//3), m) or isValid((n//3), m)
    

t = int(input())
while t>0:
    t-=1
    
    n,m = map(int,input().split())
    q = []
    q.append(n)
    res = False
    visited = set()
    while len(q):
        z = q.pop()
        visited.add(z)
        if z==m:
            res = True
            break
        if z%3 == 0:
            z /= 3
            if z not in visited:
                q.append(z)
            if (z*2) not in visited:
                q.append(z*2)
            
    if res:
        print("YES")
    else:
        print("NO")
        