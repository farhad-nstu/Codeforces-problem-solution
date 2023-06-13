t = int(input())
while t > 0:
    t -= 1
    
    inp1 = list(map(int, input().split()))
    n, x1, y1, x2, y2 = inp1[0], inp1[1], inp1[2], inp1[3], inp1[4]
    
    a = min(x1, n-x1+1)
    b = min(y1, n-y1+1)
    c = min(x2, n-x2+1)
    d = min(y2, n-y2+1)
    
    x = min(a,b)
    y = min(c,d)
    print(abs(x-y))