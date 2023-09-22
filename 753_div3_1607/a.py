t=int(input())
while t>0:
    t-=1
    letters = list(map(str, input()))
    s = input()

    res = 0
    for i in range(1, len(s)):
        # res += abs( (ord(s[i]) - ord('a') + 1) -  (ord(s[i-1]) - ord('a') + 1) )
        res += abs( (letters.index(s[i]) + 1) -  (letters.index(s[i-1]) + 1) )

    print(res)