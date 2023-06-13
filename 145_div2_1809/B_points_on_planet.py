def pointOnPlanet():
    def sqrt(n):
        if n < 2:
            return n
        low, high = 1, n
        while low <= high:
            mid = (low + high) // 2
            if mid * mid == n:
                return int(mid)
            elif mid * mid < n:
                low = mid + 1
            else:
                high = mid - 1
        return int(high)
    
    t = int(input())
    while t > 0:
        n = int(input())
        print(sqrt(n-1))
        t -= 1
    return True

pointOnPlanet()
