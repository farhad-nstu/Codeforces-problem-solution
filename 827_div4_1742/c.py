t=int(input())
while t>0:
    t-=1

    # tmp1 = input()
    # tmp2 = input()

    a = []
    for i in range(10):
        if input() == "":
            continue
        a.append(input())

    # print(a)
    # break

    res = "."

    for i in range(8):
        if a[i][0] == "R" and a[i][-1] == "R":
            res = "R"
            break
    
    if res != ".":
        print(res)
        continue

    for j in range(7, -1, -1):
        is_curr_char_R = False
        for i in range(8):
            if a[i][j] != "B":
                is_curr_char_R = True
                break
        
        if not is_curr_char_R: # as we start traversing from right side. so when we donot find any R we return result
            res = "B"
            break
    
    print(res)