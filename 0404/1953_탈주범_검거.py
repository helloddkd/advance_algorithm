import sys
sys.stdin = open('1953.txt','r')
from collections import deque

diction = {
    1: [(0, 1), (0, -1), (1, 0), (-1, 0)],
    2: [(0, 1), (0, -1)],
    3: [(1, 0), (-1, 0)],
    4: [(1, 0), (0, -1)],
    5: [(1, 0), (0, 1)],
    6: [(0, 1), (-1, 0)],
    7: [(0, -1), (-1, 0)],
}

def DFS(wow, k=0):
    if k == L:
        return
    x, y = wow[0], wow[1]
    visited[y][x] = True
    dir = arr[y][x]
    for di in diction[dir]:
        newx, newy = x + di[0], y + di[1]
        if newx < 0 or newx > X - 1 or newy < 0 or newy > Y - 1 or arr[newy][newx] == 0:
            continue
        if visited2[newy][newx]:
            continue
        temp = (di[0] * (-1), di[1] * (-1))
        if temp not in diction[arr[newy][newx]]:
            continue
        visited2[newy][newx] = True
        DFS((newx, newy), k + 1)
        visited2[newy][newx] = False


T = int(input())

for _ in range(T):
    Y, X, y, x, L = map(int, input().split())
    arr = [list(map(int, input().split())) for ___ in range(Y)]
    visited = [[False] * X for __ in range(Y)]
    cnt = 0
    visited2 = [[False] * X for __ in range(Y)]
    visited2[y][x] = True
    DFS((x, y))
    result = sum([sum(i) for i in visited])
    print('#{} {}'.format(_ + 1, result))