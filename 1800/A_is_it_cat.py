t = int(input())
while t > 0:
    t -= 1
    
    n = int(input())
    s = input()
    cat_sound = ""
    
    for c in s:
        if not cat_sound or c.upper() != cat_sound[-1]:
            cat_sound += c.upper()

    if cat_sound == "MEOW":
        print("YES")
    else:
        print("NO")