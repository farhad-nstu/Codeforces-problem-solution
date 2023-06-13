t = int(input())
while t > 0:
    t -= 1
    a,b,c,d = map(int, input().split())
    if a==c and b==d:
        print(0)
        continue
    
    diff_in_y = d-b
    if b>d or c-a > diff_in_y:
        print(-1)
        continue
    
    res = (a-c) + 2*diff_in_y
    print(res)