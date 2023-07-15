t=int(input())
while t>0:
    t-=1
    
    n = int(input())
    a = list(map(int,input().split()))

    for i in range(1,n):
        if a[i-1] == 1:
            a[i-1] = a[i-1] + 1
        
        if a[i] == 1:
            a[i] = a[i] + 1
            
        if (a[i] % a[i-1]) == 0:
            a[i] = a[i] + 1

    print(" ".join(str(i) for i in a))