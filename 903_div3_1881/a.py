t=int(input())
while t>0:
    t-=1

    n, m = map(int, input().split())
    x = input()
    s = input()

    count = 0
    if s in x:
        print(count)
        continue 

    status = False
    while len(x) <= 25:
        count += 1
        x += x
        if s in x:
            status = True
            break
    
    if status:
        print(count)
    else:
        print(-1)