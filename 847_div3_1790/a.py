t=int(input())
while t>0:
    t-=1

    s = input()
    n = len(s)
    S = "314159265358979323846264338327"

    if s == S:
        print(30)
        continue

    count = 0
    for i in range(n):
        if s[i] == S[i]:
            count += 1
        else:
            break
    print(count)