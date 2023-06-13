t = int(input())
while t>0:
    t-=1
    n = int(input())
    s = input()
    
    res_set = []
    for i in range(1,n):
        pair = s[i-1] + s[i]
        if pair not in res_set:
            res_set.append(pair)
    print(len(res_set))