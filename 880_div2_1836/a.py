from collections import Counter
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

    # print(count)
    
    status = True
    for i, v in enumerate(count):
        # print(i, v)
        # break

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

    # # curr_val = a[0]
    # if a[0] != 0:
    #     print("NO")
    #     continue

    # status = True
    # for i in range(1, n):
    #     if a[i] > a[i-1] + 1:
    #         status = False
    #         break
    
    # if not status:
    #     print("NO")
    # else:
    #     print("YES")
            
            