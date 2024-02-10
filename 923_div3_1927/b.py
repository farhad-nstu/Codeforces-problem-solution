t=int(input())
while t>0:
    t-=1

    n=int(input())
    s = input().replace(" ", "")
    last_char = 97
    last_zero_char = 97
    cache = {}
    res = ''
    for c in s:
        if c == '0':
            res += chr(last_char)
            last_char += 1
        elif c == '1':
            res += chr(last_zero_char)
            cache[int(c)] = last_zero_char
            last_zero_char += 1
        else:
            res += chr(cache[int(c)-1])
            cache[int(c)] = cache[int(c)-1]

    print(res)
