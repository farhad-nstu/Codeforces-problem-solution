t=int(input())
while t > 0:
    t -= 1
    a = list(map(int, input().split()))
    n = len(a)
    max_val = max(a)
    final_res = []
    for i in range(n//2 + 1):
        sum_ = a[i]
        res = [a[i]]
        is_found = False
        for j in range(i+1, n//2 + 1):
            sum_ += a[j]
            res.append(a[j])
            if len(res) == 3 and sum_ == max_val:
                is_found = True
                break
            elif len(res) >= 3 and sum_ != max_val:
                res.pop()
                sum_ -= a[j]
                # continue
            
        if is_found:
            final_res = res
            break
    
    print(" ".join(str(i) for i in final_res))
            