n= int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
m= int(input())
c = list(map(int, input().split()))
d = list(map(int, input().split()))

x = 1
for i in range(n):
    x *= a[i]**b[i]

y = 1
for i in range(m):
    y *= c[i]**d[i]

if x > y:
    p = y
    q = x
else:
    p = x
    q = y

count = p
while count < q:
    if count * 

