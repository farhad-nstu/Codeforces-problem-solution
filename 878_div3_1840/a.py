t=int(input())
while t>0:
    t-=1
    
    n = int(input())
    s = input()
    
    i = 1
    curr = s[0]
    tmp = ""
    while i < n:
        if s[i] == curr:
            tmp += s[i]
            if i < n-1:
                curr = s[i+1]
                i += 1
        i += 1
    print(tmp)