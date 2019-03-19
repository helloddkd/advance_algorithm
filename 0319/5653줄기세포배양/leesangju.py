from collections import deque
import sys
sys.stdin = open("5653.txt", "r")


T = int(input())
for test_case in range(1, T+1 ):

    # 세로, 가로, 시간
    N, M, K = map(int, input().split())

    # 델타를 사용하였습니다.
    dxy = [[0, 1], [0, -1], [1, 0], [-1, 0]]

    # 초기 줄기세포의 분포를 저장할 2차원 리스트 arr
    arr = []
    for n in range(N):
        arr += [list(map(int, input().split()))]

    # visit 역할을 하는 2차원 리스트, 이미 세포가 있는 곳에 또 세포가 생기는 것을 방지, 범위는 넉넉하게 잡았습니다.
    already_filled = [[False for _ in range(M+2*K+2)] for _ in range(N+2*K+2)]

    # 생명력이 큰 세포가 우선되어 번식해야 하므로 그 순서대로 deque 저장하기 위해 필요한 리스트를 만들었습니다.
    stem_cells = [[] for _ in range(11)]
    for i in range(N):
        for j in range(M):
            if arr[i][j] > 0:
                stem_cells[arr[i][j]] += [(i, j)]

    # 세포의 위치, 생명력, 활성화에 필요한 시간을 저장하는 deque들
    cells = deque()
    life_span = deque()
    activate_time = deque()

    # 생명력이 큰 줄기세포부터 각각의 deque에 정보를 저장해주었습니다.
    for idx in range(10, 0, -1):
        if len(stem_cells[idx]) > 0:
            for location in stem_cells[idx]:
                already_filled[location[0]][location[1]] = True
                cells.append(location)
                life_span.append(idx)
                activate_time.append(idx)

    # 시간만큼 for문을 돌립니다.
    for k in range(K):

        # 한 시간이 지날때 원래 있는 세포만큼만 돌아야 하므로 그 값을 저장하여 for 문을 돌린다.
        original_cells = len(cells)

        for R in range(original_cells):

            C = cells.popleft()
            L = life_span.popleft()
            IA = activate_time.popleft()

            # 아직 활성화 되는데 시간이 필요하다면 다시 집어 넣습니다.
            if IA > 0:
                cells.append((C[0], C[1]))
                life_span.append(L)
                activate_time.append(IA-1)

            # 활성화가 되었다면 해당 위치에서 델타값을 사용하여 번식된 세포들을 저장해줍니다. 이때 이미 세포가 있는 위치라면 안되도록 합니다.
            elif IA == 0:
                for delta in dxy:
                    if not already_filled[C[0] + delta[0]][C[1] + delta[1]]:
                        already_filled[C[0] + delta[0]][C[1] + delta[1]] = True
                        cells.append((C[0] + delta[0], C[1] + delta[1]))
                        life_span.append(L)
                        activate_time.append(L)

                if L - 1 > 0:
                    cells.append((C[0], C[1]))
                    life_span.append(L-1)
                    activate_time.append(-1)

            # 이미 활성화되고 번식한 세포의 경우, 수명이 남아있다면 수명을 하나 빼주고 다시 추가해줍니다.
            elif IA < 0:
                if L - 1 > 0:
                    cells.append((C[0], C[1]))
                    life_span.append(L-1)
                    activate_time.append(-1)

    print("#{} {}".format(test_case, len(cells)))