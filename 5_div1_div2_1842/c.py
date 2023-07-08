t=int(input())
while t>0:
    t-=1
    
    n = int(input())
    a = list(map(int, input().split()))
    
    res = 0
    i = 0
    while i < len(a):
        j = i+1
        while j < len(a):
            if a[j] == a[i]:
                if j+1 < len(a) and a[j+1] == a[i]:
                    j += 1
                    continue
                a = a[:i] + a[j+1:]
                i = 0
                j = 0
                break
            j += 1
        i += 1
    # print(a)
    print(n-len(a))
        