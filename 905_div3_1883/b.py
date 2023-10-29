from collections import Counter
t=int(input())
while t>0:
    t-=1

    n, k = map(int, input().split())
    s = input()
    count = Counter(s)
        
    odd = 0
    for v in count:
        if count[v] % 2 != 0:
            odd += 1
    
    if odd - 1 < 0:
        odd = 0
    else:
        odd -= 1

    if k >= odd:
        print("YES")
    else:
        print("NO")