t = int(input())
while t > 0:
    n = int(input())
    s = input()
    status = True
    last = {}
    for i in range(n):
        if s[i] in last and last[s[i]] == list(last.items())[-1][0]:
            last[s[i]] = i
        else:
            if s[i] in last and (i-last[s[i]])%2 == 1:
                status=False
                break
            last[s[i]] = i

    # print(last[s[0]], " ", last[s[1]])
    # break
    if status:
        print("YES")
    else:
        print("NO")
    
    t -= 1