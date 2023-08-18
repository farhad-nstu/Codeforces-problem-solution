t=int(input())
while t>0:
    t-=1
    
    a,b,c = map(int,input().split())
    
    if a == b:
        if c%2:
            print("First")
        else:
            print("Second")
    elif a > b:
        print("First")
    else:
        print("Second")