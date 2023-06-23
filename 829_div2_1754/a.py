from collections import Counter
t=int(input())
while t>0:
    t-=1
    
    n=int(input())
    s = input()
    
    if s[-1] == "Q":
        print("No")
        continue
    
    # a = 0
    # q = 0
    # status = True
    # for i in range(n-1, -1, -1):
    #     if s[i] == 'A':
    #         a += 1
    #     else:
    #         a -= 1
    #         if a<0:
    #             status = False

    # if status:
    #     print("Yes")
    # else:
    #     print("No")
    
    # another way
    q = []
    for i in range(n):
        if s[i] == 'Q':
            q.append(s[i])
        else:
            if len(q):
                q.pop()

    if len(q):
        print("No")
    else:
        print("Yes")
        
        
        
    
    # QAQAQAAQ // No
    # QAAQQQAA // NO
    