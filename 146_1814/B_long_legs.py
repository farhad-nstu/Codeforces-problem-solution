t=int(input())
while t>0:
    t-=1
    
    arr = list(map(int,input().split()))
    a, b = arr[0], arr[1]
    res = 100000 # max value
    
    for i in range(1, 100000+1): #10**5
        tmp = i - 1 + (a+i-1)//i + (b+i-1)//i
        res = min(res, tmp)
    
    print(int(res))