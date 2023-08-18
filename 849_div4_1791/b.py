t=int(input())
while t>0:
    t-=1
    
    n = int(input())
    s = input()

    ud_count, lr_count = 0, 0
    is_candy = False

    for c in s:
        if c == "U":
            ud_count += 1
            if ud_count == 1 and lr_count == 1:
                is_candy = True
                break
        elif c == "D":
            ud_count -= 1
            if ud_count == 1 and lr_count == 1:
                is_candy = True
                break
        elif c == "R":
            lr_count += 1
            if ud_count == 1 and lr_count == 1:
                is_candy = True
                break
        elif c == "L":
            lr_count -= 1
            if ud_count == 1 and lr_count == 1:
                is_candy = True
                break
    
    if is_candy:
        print("YES")
    else:
        print("NO")