t=int(input())
while t>0:
    t-=1
    
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    a_sum, b_sum = sum(a), sum(b)
    if a_sum > b_sum:
        print('Tsondu')
    elif b_sum > a_sum:
        print('Tenzing')
    else:
        print('Draw')
        