t=int(input())
while t>0:
    t-=1

    a = list(map(int, input().split()))

    minVal = min(a)
    for i in range(len(a)):
        if a[i] != minVal:
            first_part = a[:i]
            tmp = a[i]
            second_part = a[i+1:]
            a = first_part + [minVal] + [a[i] - minVal] + second_part
            break
    
    for i in range(len(a)):
        if a[i] != minVal:
            first_part = a[:i]
            tmp = a[i]
            second_part = a[i+1:]
            a = first_part + [minVal] + [a[i] - minVal] + second_part
            break
    
    for i in range(len(a)):
        if a[i] != minVal:
            first_part = a[:i]
            tmp = a[i]
            second_part = a[i+1:]
            a = first_part + [minVal] + [a[i] - minVal] + second_part
            break

    status = True
    for i in range(1, len(a)):
        if a[i] != a[i-1]:
            status = False
            break
    
    if status:
        print("YES")
    else:
        print("NO")