# t = int(input())
# while t > 0:
#     t-=1
    
#     n = int(input())
#     arr1 = list(map(int, input().split()))
#     arr2 = list(map(int, input().split()))
#     status = False
#     for i in range(n-1, -1, -1):
#         tmp = arr1[i]
#         arr1[i] = arr2[i]
#         arr2[i] = tmp
#         if arr1[-1] == max(arr1) and arr2[-1] == max(arr2):
#             status = True
#             break 
#     if status:
#         print("Yes")
#     else:
#         print("No")


t = int(input())
while t > 0:
    t-=1
    
    n = int(input())
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))
    
    status = True
    for i in range(n):
        if (arr1[i] <= arr1[n-1] and arr2[i] <= arr2[n-1]) or (arr1[i] <= arr2[n-1] and arr2[i] <= arr1[n-1]):
            continue
        else:
            status = False
            break 
    if status:
        print("Yes")
    else:
        print("No")