t = int(input())
while t>0:
    t-=1
    
    arr = list(map(int,input().split()))
    n,k = arr[0],arr[1]
    s = input()
    
    charArr = [chr(c) for c in range(65,91)]
    charArr += [chr(c+32) for c in range(65,91)]
    c_count = {}
    for c in charArr:
        c_count[c] = 0

    for c in s:
        c_count[c] += 1
    
    res = 0
    for c in range(65, 91):
        min_to_add = min(c_count[chr(c)], c_count[chr(c+32)])
        c_count[chr(c)] -= min_to_add
        c_count[chr(c+32)] -= min_to_add
        res += min_to_add

    for c in range(65, 91):
        max_to_add = max(c_count[chr(c)], c_count[chr(c+32)])
        min_add = min(k, max_to_add//2)
        res += min_add
        k -= min_add
    
    print(res)