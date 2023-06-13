n = int(input())
res = 0
for i in range(n):
    s = input()
    arr_s = s.split()
    arr_int = list(map(int,arr_s))
    if sum(arr_int) >= 2:
        res += 1
print(res)