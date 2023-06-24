t=int(input())
while t>0:
    t -= 1
    
    n, x = map(int,input().split())
    
    if n%x:
        print(-1) # if not divisibly by x then not exist permutation
        continue
    
    a = [0] * (n+1)
    a[1], a[n] = x, 1
    
    for i in range(2, n):
        a[i] = i
    
    if n==x:
        print(" ".join(str(a[i]) for i in range(1,n+1))) # if n==x as usual print the array
        continue
    
    a[x] = n
    for i in range(2, n):
        if (i%x == 0) and (n%i == 0):
            a[x], a[i] = a[i], a[x]
            x = i
    
    print(" ".join(str(a[i]) for i in range(1, n+1)))