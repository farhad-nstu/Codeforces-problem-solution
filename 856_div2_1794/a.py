t=int(input())
while t>0:
    t-=1
    
    n = int(input())
    a = list(map(str,input().split()))

    s1, s2 = "", ""
    for i in range(2*n-2):
        if len(a[i]) == n-1:
            if not s1:
                s1 = a[i]
            else:
                s2 = a[i]
    
    status1, status2 = True, True
    for i in range(1,n-1):
        if s1[i] != s2[i-1]:
            status1 = False
            # prefix = s2
            # suffix = s1
        if s2[i] != s1[i-1]:
            status2 = False
    
    if status1:
        prefix = s1
        suffix = s2
    else:
        prefix = s2
        suffix = s1

    S = prefix[0] + suffix
    
    if S == S[::-1]:
        print("YES")
    else:
        print("NO")
        