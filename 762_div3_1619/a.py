t=int(input())
while t>0:
    t-=1

    s = input()
    n = len(s)
    if n%2:
        print("NO")
        continue

    mid = n//2
    substr1 = s[:mid]
    substr2 = s[mid:]
    if substr1 == substr2:
        print("YES")
    else:
        print("NO")
