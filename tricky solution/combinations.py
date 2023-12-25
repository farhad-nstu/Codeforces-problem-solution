class Solution:
    def factorial(self, n: int):
        if n <= 1:
            return 1 
        return n * self.factorial(n-1)

    def combination_of_number(self, n: int, r: int):
        return int(self.factorial(n) / (self.factorial(r) * self.factorial(n-r)))

    def combine(self, n: int, k: int):
        combs = []
        def combinations(i, comb):
            if len(comb) == k:
                combs.append(comb[:])
                return
            
            for j in range(i, n):
                comb.append(j+1)
                combinations(j+1, comb)
                comb.pop()

        combinations(0, [])
        return combs

obj = Solution()
print(obj.combination_of_number(5, 3))
print(obj.combine(5, 3))