t=int(input())
while t>0:
    t-=1
    l, r, a = map(int, input().split())

    if a == 1:
        print(r)
        continue

    maxVal = (r // a) + (r % a)

    tmp = r - (r%a) - 1
    if tmp >= l:
        x = tmp
    else:
        x = r

    maxVal1 =  (x // a) + (x % a)
    maxVal = max(maxVal, maxVal1)

    print(maxVal)