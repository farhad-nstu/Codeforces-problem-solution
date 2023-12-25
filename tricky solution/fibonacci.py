# # dp
# n = 5
# dp = [0] * (n+1)
# dp[1] = 1
# for i in range(2, n+1):
#     dp[i] = dp[i-1] + dp[i-2]
# print(" ".join(str(i) for i in dp))



# Recursion
def fib(n):
    if n <= 1:
        return n 
    return fib(n-1) + fib(n-2)

n = 5
for i in range(n+1):
    print(fib(i))



# Another Recursion with dp
# a = {0:0, 1:1}
# def fib(n):
#     if n in a:
#         return a[n]
#     fib_n = fib(n-1) + fib(n-2)
#     a[n] = fib_n
#     return a[n]
# fib(5)
# print(list(a.values()))