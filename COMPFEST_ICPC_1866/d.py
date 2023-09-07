n,m,k = map(int, input().split())
a = []
for i in range(n):
    a += list(map(int, input().split()))

# a.sort()
res = 0
operationNumber = m - k + 1
# while len(a) > 0 and operationNumber > 0:
#     res += a.pop()
#     operationNumber -= 1
# print(res)
for p in range(operationNumber):
    maxVal = max(a)
    idx = a.index(maxVal)
    if idx >= m:
        y = len(a) - idx - m - 1 
    else:
        y = idx

    if p ==1:
        print(res, maxVal, idx, y)
        break

    if p <= y and y <= (p+k-1):
        res += maxVal
        a[y] = 0

print(res)