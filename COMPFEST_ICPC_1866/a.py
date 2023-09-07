n= int(input())
a = list(map(int, input().split()))
minVal = float("inf")
for i in range(n):
    minVal = min(minVal, abs(a[i]))
print(minVal)