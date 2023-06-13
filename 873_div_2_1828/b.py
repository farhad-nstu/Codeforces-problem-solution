def gcd(a, b):
    if(b == 0):
        return a
    else:
        return gcd(b, a % b)
    
t = int(input())
while t > 0:
    t -= 1
    
    n = int(input())
    a = list(map(int, input().split()))
    res = 0
    for i in range(n):
        res = gcd(res, abs(a[i]-(i+1)))
    print(res)
    
    
    # 3 4 1 2  res = 0, 2, 2, 2, 2
    # gcd(0, abs(3-(0+1))) => gcd(0, 2) = 2
    # gcd(2, abs(4-(1+1))) => gcd(2, 2) = 2
    # gcd(2, abs(4-(1+1))) => gcd(2, 2) = 2
    # gcd(2, abs(2-(3+1))) => gcd(2, 2) = 2
    
    # def gcd(a, b):
    # if(b == 0):
    #     return a
    # else:
    #     return gcd(b, a % b)
    
    # 4 2 6 7 5 3 1
    # gcd(0, abs(4-(0+1))) => gcd(0, 3) = 3
    # gcd(3, abs(2-(1+1))) => gcd(3, 0) = 3
    # gcd(3, abs(6-(2+1))) => gcd(3, 3) = 3
    # gcd(3, abs(7-(3+1))) => gcd(3, 3) = 3
    # gcd(3, abs(5-(4+1))) => gcd(3, 0) = 3
    # gcd(3, abs(3-(5+1))) => gcd(3, 3) = 3
    # gcd(3, abs(1-(6+1))) => gcd(3, 6) = 3
    
    # 1 5 3 4 2 6
    # gcd(0, abs(1-(0+1))) => gcd(0, 0) = 0
    # gcd(0, abs(5-(1+1))) => gcd(0, 3) = 3
    # gcd(3, abs(3-(2+1))) => gcd(3, 0) = 3
    # gcd(3, abs(4-(3+1))) => gcd(3, 0) = 3
    # gcd(3, abs(2-(4+1))) => gcd(3, 3) = 3
    # gcd(3, abs(6-(5+1))) => gcd(3, 0) = 3