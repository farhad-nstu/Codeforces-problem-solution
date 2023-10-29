t=int(input())
while t>0:
    t-=1
    
    n = int(input())
    a = list(map(int,input().split()))
    a.sort()

    if a[0] != 0:
        print("NO")
        continue

    count = {}
    for i in range(n):
        if a[i] not in count:
            count[a[i]] = 1
        else:
            count[a[i]] += 1
    
    status = True
    for i, v in enumerate(count):
        if i != v:
            status = False
            break

        if (i + 1) in count and (count[i] < (count[i+1])):
            status = False
            break
    
    if not status:
        print("NO")
    else:
        print("YES")
            
            