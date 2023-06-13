def xor(n):
    x = 2
    for i in range(n):
        x ^= i
    return x 
print(xor(3))

# def xor(n):
#     if n%4 == 0:
#         return n
#     elif n%4 == 1:
#         return 1
#     elif n%4 == 2:
#         return n + 1
#     else:
#         return 0
# print(xor(4))
        