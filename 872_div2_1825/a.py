t=int(input())
while t>0:
    t-=1

    s = input()
    if s != s[::-1]:
        print(len(s))
        continue 

    new_s = s[1:]
    if new_s != new_s[::-1]:
        print(len(new_s))
    else:
        print(-1)