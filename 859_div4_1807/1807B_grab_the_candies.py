t = int(input())
while t > 0:
    n = int(input())
    arr = list(map(int, input().split()))
    mihai_candy, bianca_candy = 0, 0
    for i in range(n):
        if arr[i] % 2:
            bianca_candy += arr[i]
        else:
            mihai_candy += arr[i]
    print("YES") if mihai_candy > bianca_candy else print("NO")
    t -= 1