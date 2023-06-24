t=int(input())
while t>0:
    t-=1
    
    s = input()
    n = len(s)
    
    if s in ['Yess','YES','se']:
        print('NO')
        continue
    
    status = True
    for i in range(n):
        if s[i] not in ['Y','e','s']:
            status = False
        if i < n-1:
            if s[i] == "Y" and s[i+1] != "e":
                status = False
            elif s[i] == "e" and s[i+1] != "s":
                status = False
            elif s[i] == "s" and s[i+1] != "Y":
                status = False
    
    if status:
        print("YES")
    else:
        print("NO")
        