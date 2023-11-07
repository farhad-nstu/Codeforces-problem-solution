t=int(input())
while t>0:
    t-=1
    n = int(input())
    s1 = input()
    s2 = input()
    status = True
    for i in range(n):
        if s1[i] != s2[i]:
            if not (s1[i] in ['G','B'] and s2[i] in ['G','B']):
                status = False
                break
    if status:
        print("YES")
    else:
        print("NO")