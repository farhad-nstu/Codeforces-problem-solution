t=int(input())
while t>0:
    t-=1

    n=int(input())
    s = input()
    start = 0
    end = 0
    for i in range(n):
        if s[i] == 'B':
            if not start:
                start = i+1
                end = i+1
            else:
                end = i+1
    print(end - start + 1)
