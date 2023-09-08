t=int(input())
while t>0:
    t-=1
    s = input()
    c = input()

    if c not in s:
        print("NO")
        continue
    
    if len(s) <= 2 and c in s:
        print("YES")
        continue

    status = False
    for i in range(len(s)):
        if s[i] == c and ((i+1)%2 != 0):
            status = True
            break
    if status:
        print("YES")
    else:
        print("NO")