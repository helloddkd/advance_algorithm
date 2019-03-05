import sys
sys.stdin = open('5188.txt', 'r')

t = int(input())
for test in range(t):
    N = int(input())
    arr = []
    for _ in range(N):
        arr.append(list(map(int, input().split())))
    see = [[0 for _ in range(N)] for i in range(N)]
    see[0][0] = arr[0][0]

    for i in range(N):
        for j in range(N):
            if j > 0 and i != 0:
                see[j][i] = min(see[j - 1][i], see[j][i - 1]) + arr[j][i]
            elif j == 0:
                see[j][i] = see[j][i - 1] + arr[j][i]
            elif i == 0 and j != 0:
                see[j][i] = see[j - 1][i] + arr[j][i]

    print(f'#{test+1} {see[-1][-1]}')
