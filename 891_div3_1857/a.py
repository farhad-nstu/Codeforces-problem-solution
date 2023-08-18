t=int(input())
while t>0:
    t-=1

    n = int(input())
    a = list(map(int,input().split()))
    
    even_sum = 0
    odd_sum = 0

    for i in a:
        if i%2:
            odd_sum += i
        else:
            even_sum += i
    
    if even_sum%2 == 0 and odd_sum%2 == 0:
        print("YES")
    else:
        print("NO")