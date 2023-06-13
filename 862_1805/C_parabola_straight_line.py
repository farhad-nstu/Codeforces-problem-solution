def binarySearch(data, val):
    highIndex = len(data)-1
    lowIndex = 0
    while highIndex > lowIndex:
            index = (highIndex + lowIndex) // 2
            sub = data[index]
            if data[lowIndex] == val:
                    return [lowIndex, lowIndex]
            elif sub == val:
                    return [index, index]
            elif data[highIndex] == val:
                    return [highIndex, highIndex]
            elif sub > val:
                    if highIndex == index:
                            return sorted([highIndex, lowIndex])
                    highIndex = index
            else:
                    if lowIndex == index:
                            return sorted([highIndex, lowIndex])
                    lowIndex = index
    return sorted([highIndex, lowIndex])
 
t = int(input())
while t > 0:
    t -= 1
    
    inp1 = list(map(int, input().split()))
    n, m = inp1[0], inp1[1]
    
    arr_lines = []
    for _ in range(n):
        arr_lines.append(int(input()))
    
    arr_lines.sort()
        
    arr_parabolas = []
    for _ in range(m):
        arr_parabolas.append(list(map(int, input().split())))
    
    for p in arr_parabolas:
        a, b, c = p[0], p[1], p[2]
        
        # find out k closeset to b
        # k_closest_to_b_idx = n+1
        # for i in range(1, n):
        #     if abs(b - arr_lines[i]) < abs(b - arr_lines[k_closest_to_b_idx]):
        #         k_closest_to_b_idx = i
        # k = arr_lines[k_closest_to_b_idx]
        
        # k_closest_to_b_idx = 0
        # l, r = 0, n
        # while l < r:
        #     mid = (l+r) // 2
        #     if b == arr_lines[mid]:
        #         k_closest_to_b_idx = mid
        #         break
        #     elif b > arr_lines[mid]:
        #         l = mid + 1
        #     else:
        #         r = mid
                
        #     if l == r:
        #         if abs(b - arr_lines[l]) < abs(b - arr_lines[r]):
        #             k_closest_to_b_idx = l 
        #         else:
        #             k_closest_to_b_idx = r
        #     k = arr_lines[k_closest_to_b_idx]        
        
        k_s = binarySearch(arr_lines, b)
        if abs(b - arr_lines[k_s[0]]) < abs(b - arr_lines[k_s[1]]):
            k_closest_to_b_idx = k_s[0]
        else:
            k_closest_to_b_idx = k_s[1]
        k = arr_lines[k_closest_to_b_idx]
            
        
        # parabola equation
        D = (b-k)**2 - (4*a*c)
        
        if D < 0:
            print("YES")
            print(k)
        else:
            print("NO")