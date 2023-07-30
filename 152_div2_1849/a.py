t=int(input())
while t>0:
    t-=1
    
    b, c, h = map(int,input().split())
    ch = c + h
    
    
    count = 0
    
    if b <= ch:
        count = b + (b - 1)
    elif ch < b:
        count = ch + (ch + 1)  
    
    # b_taken = False
    # ch_taken = False
    # while b>0 and ch>0:
    #     if not b_taken:
    #         b -= 1
    #         count += 1
    #         b_taken = True 
    #         ch_taken = False
    #     elif not ch_taken:
    #         ch -= 1
    #         count += 1
    #         ch_taken = True
    #         b_taken = False
    print(count)