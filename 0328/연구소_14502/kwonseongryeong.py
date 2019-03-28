import sys
from collections import deque
from copy import deepcopy
sys.stdin = open('BJ14502.txt')

def search_virus(MAP):
    global Max
    array = deque()
    MAP2 = deepcopy(MAP)
    count = 0
    for i in range(N):
        for j in range(M):
            if MAP2[i][j] == 2:
                array.append([i, j])

    while len(array):
        index = array.popleft()
        XY = [[index[0] - 1, index[1]], [index[0] + 1, index[1]], [index[0], index[1] - 1], [index[0], index[1] + 1]]
        for xy in XY:
            if xy[0] in [-1, N] or xy[1] in [-1, M]:
                continue
            if MAP2[xy[0]][xy[1]] == 0:
                MAP2[xy[0]][xy[1]] = 2
                array.append([xy[0], xy[1]])

    for i in range(N):
        for j in range(M):
            if MAP2[i][j] == 0:
                count += 1
    Max = max(count, Max)
    return

for test_case in range(3):
    MAP = []
    N, M = map(int, input().split())
    Max = 0
    for i in range(N):
        MAP.append(list(map(int, input().split())))
    for i in range(N):
        for j in range(M):
            if MAP[i][j] == 0:
                MAP[i][j] = 1
                for k in range(i, N):
                    if k == i: start = j + 1
                    else: start = 0
                    for l in range(start, M):
                        if MAP[k][l] == 0:
                            MAP[k][l] = 1
                            for h in range(k, N):
                                if h == k: start2 = l + 1
                                else: start2 = 0
                                for g in range(start2, M):
                                    if MAP[h][g] == 0:
                                        MAP[h][g] = 1
                                        search_virus(MAP)
                                        MAP[h][g] = 0
                            MAP[k][l] = 0
                MAP[i][j] = 0
    print(Max)