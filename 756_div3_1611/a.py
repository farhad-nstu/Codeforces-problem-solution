t=int(input())
while t>0:
    t-=1
    s = input()

    if int(s) % 2 == 0:
        print(0)
        continue

    if int(s[0]) % 2 == 0:
        print(1)
        continue
    
    status = False
    for i in s:
        if int(i) % 2 == 0:
            status = True
            break
    
    if status:
        print(2)
    else:
        print(-1)
