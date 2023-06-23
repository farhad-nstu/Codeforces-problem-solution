from collections import Counter
t=int(input())
while t>0:
    t-=1
    
    n = int(input())
    s = input()
    c = Counter(s)
    max_val = c['1'] * c['0']
    
    # sub_str = ""
    # max_len = 0
    # for i in range(n):
    #     if not sub_str:
    #         sub_str += s[i]
    #         continue

    #     if sub_str[-1] == s[i]:
    #         sub_str += s[i]
    #     else:
    #         max_len = max(max_len, len(sub_str))
    #         sub_str = s[i]

    max_len = 0
    for i in range(n):
        max_len += 1
        if (i == n-1) or (s[i] != s[i+1]):
            max_val = max(max_val, (max_len*max_len))
            max_len = 0
    print(max_val)