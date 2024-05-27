def check_subsequence(target, source, n, m):
    i, j = 0, 0
    while i<n and j<m:
        sub_tar = target[i]
        while j<m and source[j] != sub_tar:
            j += 1
        if j<m:
            i += 1
        j += 1
    return i

t = int(input())
while t > 0:
    t -= 1
    n, m = map(int, input().split())
    a, b = input(), input()
    print(check_subsequence(a, b, n, m))