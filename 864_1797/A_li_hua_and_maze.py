t=int(input())
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
while t>0:
    t-=1
    
    inp1 = list(map(int, input().split()))
    n, m = inp1[0], inp1[1]
    inp2 = list(map(int, input().split()))
    x1, y1, x2, y2 = inp2[0], inp2[1], inp2[2], inp2[3]
    
    res = 4 # as there is 4 direction of a point
    count1, count2 = 0, 0
    for i in range(4):
        xx1 = x1 + dx[i]
        yy1 = y1 + dy[i]
        xx2 = x2 + dx[i]
        yy2 = y2 + dy[i]
        
        if xx1>0 and xx1<=n and yy1>0 and yy1<=m:
            count1 += 1
        if xx2>0 and xx2<=n and yy2>0 and yy2<=m:
            count2 += 1
    
    res = min(res, count1, count2, n, m)
    print(res)