def checkBeautiful(a, b):
    if a[0] < a[1] and b[0] < b[1] and a[0] < b[0] and a[1] < b[1]:
        return True
    return False

t=int(input())
while t>0:
    t-=1

    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    if(checkBeautiful(a, b)):
        print("YES")
        continue
    
    status = False
    for _ in range(4):
        tmp = a[0]
        a[0] = b[0]
        b[0] = b[1]
        b[1] = a[1]
        a[1] = tmp
        
        if(checkBeautiful(a, b)):
            status = True
            break
    
    if status:
        print("YES")
    else:
        print("NO")