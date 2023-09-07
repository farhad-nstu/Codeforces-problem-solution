def isPermutation(a):
    n = len(a)
    for i in range(1, n+1):
        if i not in a:
            return False
    return True

t=int(input())
while t>0:
    t-=1
    n = int(input())
    a = list(map(int, input().split()))

    seen = set()
    for i in range(n):
        while a[i] > n:
            a[i] = a[i] // 2

        if a[i] in seen:
            while a[i] > 1:
                a[i] = a[i] // 2
                if a[i] not in seen:
                    seen.add(a[i])
                    break

        seen.add(a[i])

    if isPermutation(a):   
        print("YES")
    else:
        print("NO")
