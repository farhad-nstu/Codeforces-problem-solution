t = int(input())
while t > 0:
    t -= 1
    
    n = int(input())
    a = list(map(int, input().split()))
    
    res = ["inf"] * n 
    res[0], res[n-1] = a[0], a[n-2] # first and last element remain same
    for i in range(n-2):
        min_el = min(a[i], a[i+1])
        res[i+1] = min_el
    
    print(" ".join(str(e) for e in res))