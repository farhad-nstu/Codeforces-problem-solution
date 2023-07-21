t=int(input())
while t>0:
    t-=1
    
    a = list(map(int,input().split()))
    n = len(a)
    status = False
    for i in range(n):
        is_valid = False
        for j in range(i+1, n):
            if a[i] + a[j] >= 10:
                status = True
                break
        if status:
            break
    if status:
        print("YES")
    else:
        print("NO") 