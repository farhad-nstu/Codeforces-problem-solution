t=int(input())
while t>0:
    t-=1

    s = input()
    res = abs(int(s[0]) - 1) if int(s[0]) else abs(10 - 1)

    for i in range(1, len(s)):
        if (int(s[i]) != 0) and (int(s[i-1]) != 0):
            res += abs( int(s[i]) - int(s[i-1]) )
        else:
            if (int(s[i]) == 0) and (int(s[i-1]) == 0):
                continue
            elif int(s[i]) == 0:
                res += abs(10 - int(s[i-1]))
            else:
                res += abs(10 - int(s[i]))

    print(res + 4)
