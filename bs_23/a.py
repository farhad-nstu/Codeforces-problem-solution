t=int(input())
case = 1
while t>0:
    t -= 1
    
    n, k = map(int, input().split())
    a = list(map(int,input().split()))
    
    a_sum = sum(a)
    target_sum = (n+1) * k
    res = target_sum - a_sum
    print("Case " + str(case) + ": " + str(res))
    case += 1