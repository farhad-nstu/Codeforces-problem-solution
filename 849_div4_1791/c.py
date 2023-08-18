t=int(input())
while t>0:
    t-=1
    
    n = int(input())
    bs = input()

    while bs and bs[0] != bs[-1]:
        bs = bs[1:-1]
    
    print(len(bs))