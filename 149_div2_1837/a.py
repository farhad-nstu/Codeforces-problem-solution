t=int(input())
while t>0:
    t -= 1
    a = list(map(int,input().split()))
    x,k = a[0],a[1]
    ans = 0
    moves = []
    if x%k:
        ans += 1
        moves.append(x)
    else:
        ans += 2
        moves.append(x-1)
        moves.append(1)
    strMoves = " ".join(str(i) for i in moves)
    print(ans)
    print(strMoves)