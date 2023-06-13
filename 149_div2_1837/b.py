t=int(input())
while t>0:
    t -= 1
    n=int(input())
    s = input()
    cnt,mx = 1, 1
    for i in range(1, n):
        if s[i] == s[i-1]:
            cnt += 1
        else:
            mx = max(cnt, mx)
            cnt = 1
    mx = max(cnt, mx) # if all character are same than it will not go into else condition. so again her take the max
    print(mx+1)