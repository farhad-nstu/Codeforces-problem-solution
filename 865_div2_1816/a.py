t = int(input())
while t > 0:
    t -= 1
    
    tmp = list(map(int, input().split()))
    a, b = tmp[0], tmp[1]
    
    if abs(a-b) == 1:
        print(1)
        print(a,b)
    else:
        print(2)
        print(a-1, 1) # if we + or - with a then it will not segment
        print(a, b)