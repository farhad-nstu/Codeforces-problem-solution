t=int(input())
while t>0:
    t-=1
    
    a = []
    for i in range(3):
        a.append(list(map(str,input())))

    c = ""
    for i in range(3):
        if a[0][i] != "." and a[0][i] == a[1][i] and a[0][i] == a[2][i]:
            c = a[0][i]
            break
    if c:
        print(c)
        continue
                
    for i in range(3):  
        if a[i][0] != "." and a[i][0] == a[i][1] and a[i][0] == a[i][2]:
            c = a[i][0]
            break
    if c:
        print(c)
        continue
        
    if a[0][0] != "." and a[0][0] == a[1][1] and a[0][0] == a[2][2]:
        c = a[0][0]
        print(c)
        continue
    
    if a[0][2] != "." and a[0][2] == a[1][1] and a[0][2] == a[2][0]:
        c = a[0][2]
        print(c)
        continue
    
    print("DRAW")