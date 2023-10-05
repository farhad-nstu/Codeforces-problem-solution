t=int(input())
while t>0:
    t-=1

    n, m = map(int,input().split())
    a = []
    for i in range(n):
        a.append(input())
    
    status = False
    res = "vika"
    index = 0
    for i in range(m):
        for j in range(n):
            if a[j][i] == res[index]:
                index += 1
                if index == 4:
                    status = True
                break
        
        if status:
            break

    if status:
        print("YES")
    else:
        print("NO")