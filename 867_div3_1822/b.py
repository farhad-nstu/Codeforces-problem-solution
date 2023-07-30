t=int(input())
while t>0:
    t-=1
    
    n = int(input())
    a = list(map(int,input().split()))
    a.sort()

    maxProduct = -float("inf")
    left = 0
    right = n-1
    while right > left:
        maxProduct = max(maxProduct, a[left]*a[left+1])
        maxProduct = max(maxProduct, a[right]*a[right-1])
        left += 1
        right -= 1
    print(maxProduct)