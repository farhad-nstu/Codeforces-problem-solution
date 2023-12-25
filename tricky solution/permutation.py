class Solution:
    def factorial(self, n: int):
        if n <= 1:
            return 1 
        return n * self.factorial(n-1)

    def permutation_of_number(self, n: int, r: int):
        return int(self.factorial(n) / self.factorial(n-r))

    def permute(self, n: int):
        perms = []
        def permutations(perm):
            if len(perm) == n:
                perms.append(perm[:])
                return
            
            for j in range(1, n+1):
                if j not in perm:
                    perm.append(j)
                    permutations(perm)
                    perm.pop()

        permutations([])
        return perms

obj = Solution()
print(obj.permutation_of_number(3, 3))
print(obj.permute(3))