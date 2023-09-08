t=int(input())
while t>0:
    t-=1
    n = int(input())
    a = list(map(int, input().split()))
    min_el = min(a)
    max_el = max(a)
    print(max_el - min_el)