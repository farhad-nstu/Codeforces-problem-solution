t=int(input())
while t>0:
    t-=1
    
    n, k = map(int, input().split())

    k = min(61, k)

    res = min(n+1, 2**k)
    print(res)
     