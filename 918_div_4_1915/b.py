t = int(input())
while t > 0:
    t -= 1
    a1 = list(map(str, input()))
    a2 = list(map(str, input()))
    a3 = list(map(str, input()))

    if "?" in a1:
        if "A" not in a1:
            print("A")
        elif "B" not in a1:
            print("B")
        else:
            print("C")
        continue

    if "?" in a2:
        if "A" not in a2:
            print("A")
        elif "B" not in a2:
            print("B")
        else:
            print("C")
        continue

    if "?" in a3:
        if "A" not in a3:
            print("A")
        elif "B" not in a3:
            print("B")
        else:
            print("C")
        continue
