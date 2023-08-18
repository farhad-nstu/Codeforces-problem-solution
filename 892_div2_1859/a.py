# def isDivisor(arr, e):
#     for v in arr:
#         if v%e == 0:
#             return True 
#     return False

t=int(input())
while t>0:
    t-=1

    n = int(input())
    a = list(map(int,input().split()))
    b,c = [],[]
    maxVal = max(a)
    for e in a:
        if e == maxVal:
            c.append(e)
        else:
            b.append(e)
            
        # if not b:
        #     b.append(e)
        #     continue

        # if not isDivisor(b, e):
        #     c.append(e)
        # else:
        #     b.append(e)
    
    if len(b) > 0 and len(c) > 0:
        print(len(b), len(c))
        print(" ".join(str(e) for e in b))
        print(" ".join(str(e) for e in c))
    else:
        print(-1)