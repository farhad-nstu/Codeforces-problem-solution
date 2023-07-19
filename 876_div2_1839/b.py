t=int(input())
while t>0:
    t-=1
    
    n = int(input())
    a = []
    for i in range(n):
        a.append(list(map(int,input().split())))
    
    a = sorted(sorted(a, key = lambda x : x[0]), key = lambda x : x[1], reverse = True)
    
    lamps = {}
    for i in range(n):
        if a[i][0] not in lamps:
            lamps[a[i][0]] = [a[i][1]]
        else:
            lamps[a[i][0]].append(a[i][1])
    
    received_bonus = 0
    for i in lamps:
        turned_on = 0
        for j in lamps[i]:
            if i == turned_on:
                break
            turned_on += 1
            received_bonus += j
            
    print(received_bonus)
        
    
    # for i in range(1, n+1):
    #     if i in lamps:
    #         lamps
    # print(lamps)
    # break
    
    
    # breaks = []
    # on_count_seen = []
    # received_bonus = 0
    # on_count = 0
    # i = 0
    # while i < len(a):
    #     if a[i] not in breaks:
    #         received_bonus += a[i][1]
    #         on_count_seen.append(a[i])
    #         on_count += 1
            
    #     j = len(a) - 1
    #     tmp = on_count
    #     while j > -1:
    #         if a[j][0] <= tmp:
    #             if a[j] in on_count_seen:
    #                 on_count -= 1
                
    #             breaks.append(a[j])
    #             # a.pop(j)
    #             i -= 1

    #         j -= 1
        
        # if i == 0:
        #     print(a, on_count, received_bonus)
        # if i == 1:
        #     print(a, on_count, received_bonus)
        # if i == 2:
        #     print(a, on_count, received_bonus)
        # if i == 3:
        #     print(a, on_count, received_bonus)
    #     i += 1
    # print(received_bonus)
        