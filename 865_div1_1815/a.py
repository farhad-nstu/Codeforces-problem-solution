t = int(input())
while t > 0:
    t -= 1
    
    n= int(input())
    a = list(map(int, input().split()))
    
    if n%2:
        print("YES")
        continue
    
    for i in range(1, n-1):
        tmp = a[i-1] - a[i]
        a[i] += tmp
        a[i+1] += tmp 
    
    if a[n-1] >= a[n-2]:
        print("YES")
    else:
        print("NO")