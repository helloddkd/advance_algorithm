for T in range(1, int(input()) + 1):
    N = int(input())
    arrs = []
    for _ in range(N):
        arrs.append(list(map(int, input().split())))

    for i in range(1, N):
        arrs[0][i] += arrs[0][i - 1]
        arrs[i][0] += arrs[i - 1][0]

    for i in range(1, N):
        for j in range(1, N):
            arrs[i][j] += min(arrs[i][j - 1], arrs[i - 1][j])

    print(f'#{T} {arrs[-1][-1]}')
