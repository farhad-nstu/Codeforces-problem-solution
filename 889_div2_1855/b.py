t=int(input())
while t>0:
    t-=1
    
    n= int(input())
    res = 0 
    for i in range(1,100):
        if n%i == 0:
            res += 1
        else:
            break
    print(res)