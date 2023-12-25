# Recursion
def fact(n):
    if n <= 1:
        return 1
    return n * fact(n-1)
print(fact(100))


# DP 
# n = 100
# dp = [1] * (n+1)
# for i in range(2, n+1):
#     dp[i] = i * dp[i-1]
# print(dp[n])


# dp and recursion
# dp = {}
# def factorial(n):
#     if n in dp:
#         return dp[n]
    
#     if n <= 1:
#         result = 1
#     else:
#         result = n * factorial(n-1)
    
#     dp[n] = result 
#     return dp[n]

# print(factorial(100))
