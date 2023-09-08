from collections import Counter
t=int(input())
while t>0:
    t-=1

    n = int(input())
    a = list(map(int, input().split()))

    count = Counter(a)
    status = True
    for c in count.values():
        if c > 1:
            status = False
    
    if status:
        print("YES")
    else:
        print("NO")