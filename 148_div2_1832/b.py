t=int(input())
while t>0:
    t -= 1
    inp1 = list(map(int, input().split()))
    n,k = inp1[0],inp1[1]
    a = list(map(int, input().split()))
    a.sort()
    while k > 0:
        minVal = a[0]+a[1]
        maxVal = a[-1]
        if minVal < maxVal:
            a = a[2:]
        else:
            a = a[:len(a)-1]
        k -= 1

    # print(a)
    print(sum(a))