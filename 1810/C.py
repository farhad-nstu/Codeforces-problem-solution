t = int(input())
while t > 0:
    t -= 1
    
    inp1 = list(map(int, input().split()))
    n, c, d = inp1[0], inp1[1], inp1[2]
    
    res = 0
    a = list(map(int, input().split()))
    a.sort()
    
    a = list(set(a))

    if n != len(a):
        res += c*(n-len(a)) # remove duplica and add into res of duplicat removal no
    
    if a[0] != 1:
        res += d # insert 1 at first index
        a.append(1)
    a.sort()
    
    n = len(a)
    to_add = float('inf')
    for i in range(1, n+1): # made each length permutation and calculate the cost
        missed_val = a[i-1] - i
        remove_i_to_n = n-i
        to_add = min(to_add, (c*remove_i_to_n + d*missed_val))
    
    res += to_add
    print(res)

            