t = int(input())
while t > 0:
    t -= 1

    n = int(input())
    a = []
    start = -float("inf")
    end = float("inf")
    for i in range(n):
        tmp = list(map(int, input().split()))
        if tmp[0] == 1:
            start = max(start, tmp[1])
        elif tmp[0] == 2:
            end = min(end, tmp[1])
        a.append(tmp)
    
    print(start, end)
    break

    res = []
    for i in range(start, end+1):
        status = True
        for pair in a:
            # print(pair)
            # break
            if pair[0] == 1:
                if i < pair[1]:
                    status = False
                    break
            elif pair[0] == 2:
                if i > pair[1]:
                    status = False
                    break
            elif pair[0] == 3:
                if i == pair[1]:
                    status = False
                    break
        
        if not status:
            continue
        res.append(i) 
    
    print(len(res))