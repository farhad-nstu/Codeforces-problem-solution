t=int(input())
while t>0:
    t-=1
    
    n, q = map(int,input().split())
    a = list(map(int,input().split()))
    # res = []
    for _ in range(q):
        tmp1, tmp2 = map(int,input().split())
        if tmp1 == 1:
            _sum = 0
            for i in range(n):
                if a[i] % 2:
                    a[i] = a[i] + tmp2
                _sum += a[i]
            # res.append(_sum)
            print(_sum)
        else:
            _sum = 0
            for i in range(n):
                if not a[i] % 2:
                    a[i] = a[i] + tmp2
                _sum += a[i]
            # res.append(_sum)
            print(_sum)
    
    # for v in res:
    #     print(v)
             
    
    