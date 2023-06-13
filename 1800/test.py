def sequenceFunction():
    arr = [4,5,6,7]
    n = len(arr)
    res = []
    def getSubSequence(i, subarr):
        if i == n:
            if len(subarr) > 0:
                res.append(subarr) 
        else:
            getSubSequence(i+1, subarr) # not include next part
            getSubSequence(i+1, subarr + [arr[i]]) # include next part
        return 

    getSubSequence(0, [])
    print(res)

sequenceFunction()