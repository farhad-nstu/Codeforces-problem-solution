t = int(input())
while t>0:
    t-=1
    
    n = int(input())
    bits = []
    values = []
    for _ in range(n):
        inp = list(map(str,input().split()))
        values.append(inp[0])
        bits.append(inp[1])
    
    res = -1
    left_bit, right_bit = 0, 0
    for i in range(n):
        if int(bits[i]) == 11:
            if res == -1:
                res = int(values[i])
            else:
                res = min(res, int(values[i]))
        elif bits[i] == "10":
            if not left_bit:
                left_bit = int(values[i])
            else:
                left_bit = min(left_bit, int(values[i]))
        elif bits[i] == "01":
            if not right_bit:
                right_bit = int(values[i])
            else:
                right_bit = min(right_bit, int(values[i]))
    
    # print(res, left_bit, right_bit)
    # break
    if (left_bit and right_bit) and res == -1:
        res = left_bit + right_bit
    elif left_bit and right_bit:
        res = min(res, left_bit+right_bit)
    
    print(res)
        