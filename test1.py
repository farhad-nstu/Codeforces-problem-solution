def mergeSort(a):
    n = len(a)
    if n>1:
        mid = n // 2
        leftA = a[:mid]
        rightA = a[mid:]
        
        mergeSort(leftA)
        mergeSort(rightA)
        
        i=j=k=0
        while len(leftA) > i and len(rightA) > j:
            if leftA[i] < rightA[j]:
                a[k] = leftA[i]
                i += 1
            else:
                a[k] = rightA[j]
                j += 1
            k += 1
        
        while len(leftA) > i:
            a[k] = leftA[i]
            i += 1
            k += 1
        
        while len(rightA) > j:
            a[k] = rightA[j]
            j += 1
            k += 1
                
            
        
a = [5,3,1,8,2,4]
mergeSort(a)
print(a)
    