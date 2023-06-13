t = int(input())
while t > 0:
    t -= 1
    
    n = int(input())
    arr = list(map(int, input().split()))
    pos_count, neg_count = 0, 0
    for i in arr:
        if i >= 0:
            pos_count += 1
        else:
            neg_count += 1
    
    for i in range(1, pos_count+1):
        print(i)
    for i in range(1, neg_count+1):
        print(pos_count-i)
    
    print("\n")
    
    for i in range(neg_count):
        print("1 0")
    for i in range(1, n - (2*neg_count) + 1):
        print(i)    