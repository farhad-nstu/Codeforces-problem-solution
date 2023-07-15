t=int(input())
while t>0:
    t-=1
    
    n = int(input())
    a = list(map(int,input().split()))
    
    q = []
    length = []
    for i in range(n):
        q.append(a[i])
        while q[0] < len(q):
            q.pop(0)
        length.append(len(q))
    print(" ".join(str(i) for  i in length))