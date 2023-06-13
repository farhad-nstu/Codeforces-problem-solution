t = int(input())
while t > 0:
    t -= 1
    
    s = input()
    a = list(s)
    # a[0], a[1] = a[1], a[0]
    # print(a)
    n = len(a)
    l, r = 1, n-2
    isPalindrome = False
    while r > l:
        a[l-1], a[l] = a[l], a[l-1]
        a[r+1], a[r] = a[r], a[r+1]
        newStr = "".join(a)
        if newStr != s and newStr == newStr[::-1]:
            isPalindrome = True
            break
        l += 1
        r -= 1
    if isPalindrome:
        print("YES")
    else:
        print("NO")
    
    
    
        
        
        