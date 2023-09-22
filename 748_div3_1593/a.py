t=int(input())
while t>0:
    t-=1
    arr = list(map(int, input().split()))
    
    if arr[0] == arr[1] and arr[1] == arr[2]:
        arr = [arr[0]+1, arr[0]+1, arr[0]+1]
    elif arr[0] == arr[1] or arr[0] == arr[1] or arr[1] == arr[2]:
        arr = [max(arr) - arr[0] + 1, max(arr) - arr[0] + 1, max(arr) - arr[0] + 1]
    else:

    # max_val = max(arr)
    # if max_val == 0:
    #     print(1, 1, 1)
    #     continue

    # idx = arr.index(max_val)

    # for i in range(len(arr)):
    #     if i == idx:
    #         arr[i] = 0
    #     else:
    #         arr[i] = max_val - arr[i] + 1

    print(" ".join(str(e) for e in arr))