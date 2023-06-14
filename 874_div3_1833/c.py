t=int(input())
while t>0:
    t-=1
    
    n= int(input())
    a = list(map(int,input().split()))
    
    min_odd = 0
    for i in a:
        if i%2:
            if not min_odd:
                min_odd = i
            else:
                min_odd = min(min_odd, i)
    
    even_count = 0
    for i in range(n):
        if not a[i]%2 or a[i] > min_odd:
            even_count += 1
    
    odd_count = 0
    for i in range(n):
        if a[i]%2 or a[i] > min_odd:
            odd_count += 1
    
    if even_count == n or odd_count == n:
        print("YES")
    else:
        print("NO")
                
        