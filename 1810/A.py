# def beautifulSequence():
#     def printSubsequences(arr, index, subarr):
#         if index == len(arr):
#             if len(subarr) != 0:
#                 tmpRes.append(subarr)
#         else:
#             printSubsequences(arr, index + 1, subarr) # exclude
#             printSubsequences(arr, index + 1, 
#                                 subarr+[arr[index]]) # include
        
#         return
    
#     t = int(input())
#     while t > 0:
#         t -= 1
        
#         n = int(input())
#         arr = list(map(int,input().split()))
#         tmpRes, subarr = [], []
#         printSubsequences(arr, 0, subarr)
#         isBeautiful = False
#         for s in tmpRes:
#             for i in range(len(s)):
#                 if i+1 == s[i]:
#                     isBeautiful = True
#                     break
#             if isBeautiful:
#                 break
        
#         if isBeautiful:
#             print("YES")
#         else:
#             print("NO")
# beautifulSequence()

# above solution show TLE

t = int(input())
while t > 0:
    t -= 1
    
    n = int(input())
    arr = list(map(int,input().split()))
    isBeautiful = False
    for i in range(1, n+1):
        if arr[i-1] <= i:
            isBeautiful = True
            break
        
    if isBeautiful:
        print("YES")
    else:
        print("NO")