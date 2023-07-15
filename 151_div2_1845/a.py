t=int(input()) 
while t>0:
    t-=1
    
    n,k,x = map(int, input().split())
    
    if k==1:
        print("NO")
        continue

    if x != 1:
        print("YES")
        print(n)
        res = ""
        for i in range(n):
            res += str(1)
            if i != n-1:
                res += " "
        print(res)
        continue

    if n%2 == 0:
        print("YES")
        print(n//2)
        res = ""
        for i in range(n//2):
            res += str(2)
            if i != n//2:
                res += " "
        print(res)
        continue

    if k==2:
        print("NO")
        continue
    
    print("YES")
    print(((n-3) // 2) + 1)
    res = ""
    for i in range((n-3) // 2):
        res += str(2)
        if i != (n-3) // 2:
                res += " "
    res += str(3)
    print(res)