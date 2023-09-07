t=int(input())
while t>0:
    t-=1

    s1, s2 = map(str, input().split())

    if s1 == s2:
        print("=")
        continue

    if s1[-1] == "L":
        if (s2[-1] == "M" or s2[-1] == "S"):
            print(">")
            continue

        if len(s1) > len(s2):
            print(">")
            continue
        else:
            print("<")
            continue
    elif s1[-1] == "M":
        if s2[-1] == "S":
            print(">")
            continue
        else:
            print("<")
            continue
    elif s1[-1] == "S":
        if (s2[-1] == "M" or s2[-1] == "L"):
            print("<")
            continue

        if len(s1) > len(s2):
            print("<")
            continue
        else:
            print(">")
            continue