t = int(input())
while t > 0:
    t -= 1

    status = False
    s = list(map(str, input()))
    for i in range(1, len(s)):
        if s[i] != s[i-1]:
            tmp = s[i]
            s[i] = s[i-1]
            s[i-1] = tmp 
            status = True
            break
    
    if status:
        print("YES")
        print("".join(s))
    else:
        print("NO")