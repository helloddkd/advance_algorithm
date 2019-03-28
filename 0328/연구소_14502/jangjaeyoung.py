import sys
from itertools import combinations
from collections import deque

sys.stdin = open('14502.txt', 'r')

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def check():
    queue = deque()
    visit = [[False] * M for _ in range(N)]
    cnt = 0

    for index in virus_index:
        queue.append(index)
        visit[index[0]][index[1]] = True
        cnt += 1

    while len(queue):
        q = queue.popleft()
        test_matrix[q[0]][q[1]] = 2

        for i in range(4):
            new_x = q[0] + dx[i]
            new_y = q[1] + dy[i]

            if 0 <= new_x < N and 0 <= new_y < M and not visit[new_x][new_y] and test_matrix[new_x][new_y] != 1:
                queue.append([new_x, new_y])
                visit[new_x][new_y] = True
                cnt += 1
                if cnt >= check_cnt:
                    return 0

    safe = size - cnt - (wall_size + 3)
    return safe


N, M = map(int, input().split())
size = N * M
matrix = [list(map(int, input().split())) for _ in range(N)]

virus_index = []
wall_size = 0
empty_index = []
for i in range(N):
    for j in range(M):
        if matrix[i][j] == 2:
            virus_index.append([i, j])
        elif matrix[i][j] == 1:
            wall_size += 1
        else:
            empty_index.append([i, j])

max_safe = 0
check_cnt = size
for combination in combinations(empty_index, 3):
    test_matrix = [matrix[i][:] for i in range(N)]
    for index in combination:
        test_matrix[index[0]][index[1]] = 1

    safe = check()
    if safe > max_safe:
        max_safe = safe
        check_cnt = size - max_safe - (wall_size + 3)

print(max_safe)