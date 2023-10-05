t = int(input())
while t>0:
    t-=1
    n = int(input())

    if n%3 == 2:
        print(n//3, n//3 + 1)
    elif n%3 == 1:
        print(n//3 + 1, n//3)
    else:
        print(n//3, n//3)