t=int(input())
while t>0:
    t-=1
    n = int(input())
    s = input()
    target_s = "Timur"
    status = True
    for c in target_s:
        if c in s:
            s = s.replace(c, "", 1)
        else:
            status = False
            break
    if s == "" and status:
        print("YES")
    else:
        print("NO")