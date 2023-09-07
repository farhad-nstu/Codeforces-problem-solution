t=int(input())
while t>0:
    t-=1

    n = int(input())
    s = input()
    s = sorted(s)
    print(ord(s[-1]) - ord('a') + 1)