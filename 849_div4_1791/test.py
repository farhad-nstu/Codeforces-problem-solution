t=int(input())
while t>0:
    t-=1
    
    n = int(input())
    s = input()
    
    a = s[0]
    b = ""
    i = 1
    isDiff = False
    while i < n:
        if s[i] not in a and not isDiff:
            a += s[i]
        else:
            isDiff = True
            if s[i] not in b:
                b += s[i]
        i += 1
    
    # for b
    # b = s[i:]
    # print(a, " hg ", b)
    
    print(len(a) + len(b))