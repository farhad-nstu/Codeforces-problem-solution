t=int(input())
while t>0:
    t-=1
    
    a = list(map(int,input().split()))
    n, k = a[0], a[1]
    if not k%2 and n%2:
        print("NO")
    else:
        print("YES")