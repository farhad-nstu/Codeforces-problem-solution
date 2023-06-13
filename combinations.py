def getAllCombinations(a): 
    n = len(a)
    combs = []
    def combinations(i, comb):
        if i == n:
            if len(comb) > 0:
                combs.append(comb)
        else:
            combinations(i+1, comb)
            combinations(i+1, comb + [a[i]])
        return 
    
    combinations(0, [])
    return combs
    
a = [1,2,3,4]
print(getAllCombinations(a))
