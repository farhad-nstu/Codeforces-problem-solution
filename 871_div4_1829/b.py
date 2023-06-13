t = int(input())
while t>0:
    t-=1
    
    n = int(input())
    a = list(map(int,input().split()))
    count = 0
    tmp = 0
    for i in range(n):
        if a[i] == 0:
            tmp += 1
        elif a[i] == 1:
            count = max(count, tmp)
            tmp = 0
    count = max(count, tmp)
    print(count)