t = int(input())
while t>0:
    t-=1
    
    s = input()
    comm_s = "codeforces"
    count = 0
    for i in range(len(s)):
        if s[i] != comm_s[i]:
            count += 1
    print(count)