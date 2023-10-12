t = int(input())
while t > 0:
    t -= 1

    n = int(input())

    status = True

    if (n-3) % 3 == 0:
        if n-5 in [4, 1]:
            status = False
        x, y, z = n-5, 4, 1
    else:
        if n-3 in [2, 1]:
            status = False
        x, y, z = n-3, 2, 1
    
    if not status:
        print("NO")
    else:
        if x>0 and y >0 and z>0 and x + y + z == n:
            print("YES")
            print(x, y, z)
        else:
            print("NO")