t=int(input())
while t > 0:
    t-=1 
    
    tmp = list(map(int, input().split()))
    n, d = tmp[0], tmp[1]
    s = input()
    status = False
    for i in range(n):
        if d > int(s[i]):
            str_first_part = s[:i]
            str_second_part = s[i:]
            s = str_first_part + str(d) + str_second_part
            status = True
            break
    print(s) if status else print(s+str(d))            
            