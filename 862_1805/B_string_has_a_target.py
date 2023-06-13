t=int(input())
while t>0:
    t-=1
    
    n = int(input())
    s = input()
    
    small_el_idx = 0
    for i in range(1, n):
        if s[i] <= s[small_el_idx]:
            small_el_idx = i
            
    new_s = s[small_el_idx]
    for i in range(n):
        if i == small_el_idx:
            continue
        else:
            new_s += s[i]
    
    print(new_s)