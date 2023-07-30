def isBeautiful(a):
    for i in range(len(a)):
        if i < len(a)-1 and a[i] == a[i+1]:
            return False
    return True

t=int(input())
while t>0:
    t-=1
    
    n, m = map(int,input().split())
    a = list(map(str,input()))
    b = list(map(str,input()))
    
    tmp = a[::-1]
    for i in range(n):
        if i < n-1 and tmp[i] == tmp[i+1]:
            b += tmp[:i+1]
            break
    
    if isBeautiful(b):
        print("Yes")
        continue
    
    tmp1 = b[::-1]
    for i in range(m):
        if i < m-1 and tmp1[i] == tmp1[i+1]:
            a += tmp1[:i+1]
            break
    
    if isBeautiful(a):
        print("Yes")
        continue
    
    print("NO")