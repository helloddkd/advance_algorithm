from collections import deque
from copy import deepcopy
import sys
sys.stdin = open("acm_14502.txt", "r")

N, M = map(int, input().split())

# delta를 사용하였습니다.
dxy = [[1, 0], [-1, 0], [0, 1], [0, -1]]

# 초기 벽, 바이러스 위치 정보를 저장할 2차원 배열 lab을 만들었습니다.
lab = []
for n in range(N):
    lab += [list(map(int, input().split()))]

# 바이러스의 위치를 queue에 넣어줬습니다.
# visit를 사용하여 이동할 수 없는 벽과 바이러스의 위치를 표시해줬습니다.
virus = deque()
visit = [[False for _ in range(M)] for _ in range(N)]
# zero는 0으로 표시된 지나갈 수 있는 통로입니다.
zero = []

for i in range(N):
    for j in range(M):
        if lab[i][j] == 0:
            zero += [[i, j]]
        elif lab[i][j] == 1:
            visit[i][j] = True
        elif lab[i][j] == 2:
            visit[i][j] = True
            virus.append([i, j])

# deepcopy를 사용하여 사용한 결과가 유지되지 않게 해주었습니다.
virus_duplicate = deepcopy(virus)
visit_duplicate = deepcopy(visit)

# zero에서 3개를 선택하여 벽을 설치하는 for문 입니다. 복제된 visit에 표시해줬습니다.
MAX = 0
for wall_1 in range(len(zero)):
    for wall_2 in range(wall_1 + 1, len(zero)):
        for wall_3 in range(wall_2 + 1, len(zero)):
            visit_duplicate[zero[wall_1][0]][zero[wall_1][1]] = True
            visit_duplicate[zero[wall_2][0]][zero[wall_2][1]] = True
            visit_duplicate[zero[wall_3][0]][zero[wall_3][1]] = True

            #
            while len(virus_duplicate) > 0:
                Q = virus_duplicate.popleft()
                for delta in dxy:
                    if 0 <= Q[0] + delta[0] < N and 0 <= Q[1] + delta[1] < M:
                        if lab[Q[0] + delta[0]][Q[1] + delta[1]] == 0 and not visit_duplicate[Q[0] + delta[0]][Q[1] + delta[1]]:
                            virus_duplicate.append([Q[0] + delta[0], Q[1] + delta[1]])
                            visit_duplicate[Q[0] + delta[0]][Q[1] + delta[1]] = True

            SUM = 0
            for L in visit_duplicate:
                SUM += sum(L)

            if N*M - SUM > MAX:
                MAX = N*M - SUM

            visit_duplicate = deepcopy(visit)
            virus_duplicate = deepcopy(virus)

print(MAX)