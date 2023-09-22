t=int(input())
while t>0:
    t-=1

    n, k = map(int, input().split())
    s = list(map(str, input()))
    
    count = 0
    # if "B" not in s:
    #     print(count)
    #     continue

    # for i in range(n):
    i = 0
    while i < n:
        if s[i] == "B":
            
            # first = s[:i]
            # tmp = s[i:i+k]
            # last = s[i+k:]

            # print(first, tmp, last)
            # break

            # for j in range(len(tmp)):
            #     tmp[j] = "W"

            # print(first, tmp, last)
            # break

            # s = first + tmp + last
            count += 1
            i += k
        else:
            i += 1
    
    print(count)