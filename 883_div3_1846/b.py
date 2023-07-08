t=int(input())
while t>0:
    t-=1
    
    s1 = input()
    s2 = input()
    s3 = input()

    for i in range(3):
        if s1[i] == s2[i] and s1[i] == s3[i]:
            c = s1[i]
            
    if s1[0] == s1[1] and s1[0] == s1[2]:
        c = s1[0]
    
    if s2[0] == s2[1] and s2[0] == s2[2]:
        c = s2[0]
    
    if s3[0] == s3[1] and s3[0] == s3[2]:
        c = s3[0]
        
    if s1[0] == s2[1] and s1[0] == s3[2]:
        c = s1[0]
    
    if s3[0] == s2[1] and s3[0] == s1[2]:
        c = s3[0]
    
    if c == ".":
        print("DRAW")
    else:
        print(c)