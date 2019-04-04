import sys
sys.stdin = open("2105.txt", "r")

# 왼쪽 위부터 시작하여 한 칸씩 진행하며 가능한 경우의 수를 모두 구하는 방법을 사용하였습니다.
# 델타를 사용하였습니다.
dxy = [[1, 1], [1, -1], [-1, -1], [-1, 1]]

# 해당 위치에서 경우의 수를 구하고 전역변수 maximum에 반영하는 함수입니다. 처음 시작할 때 2개의 카페를 지나온 상태에서 진행하므로 cnt의 기본값은 2입니다.
def desert_tour(x, y, delta, visit, cnt=2):
    global MAXIMUM

    # 만약, 다음에 도착할 위치가 처음 시작 위치가 된다면, return하고 지금까지 지나쳐온 카페의 수를 maximum과 비교, 저장합니다.
    if x - 1 == i and y + 1 == j:
        if cnt > MAXIMUM:
            MAXIMUM = cnt
        return

    # delta의 경우, 0일때는 ↘ 1일때는 ↙ 2일때는 ↖ 3일때는 ↗ 방향으로 진행합니다.
    # 진행방향이 ↘ 일때는, ↘ 또는 ↙로 진행할 수 있으므로 범위를 만족하며 디저트 종류의 값이 중복되지 않는 경우를 만족하면 각각의 경우를 재귀로 실행합니다.
    if delta == 0:
        if 0 <= x + 1 < N and 0 <= y + 1 < N and not visit[cafes[x+1][y+1]]:
            new_visit = visit[:]
            new_visit[cafes[x+1][y+1]] = True
            # 새로 한번 진행할 때마다, 지나쳐온 카페의 수(cnt)에 1을 더해줍니다.
            desert_tour(x + 1, y + 1, 0, new_visit,cnt+1)
        if 0 <= x + 1 < N and 0 <= y - 1 < N and not visit[cafes[x+1][y-1]]:
            new_visit = visit[:]
            new_visit[cafes[x + 1][y - 1]] = True
            desert_tour(x + 1, y - 1, 1, new_visit, cnt+1)
    # 진행방향이 ↙ 일때는, ↙ 또는 ↖로 진행할 수 있습니다.
    elif delta == 1:
        if 0 <= x + 1 < N and 0 <= y - 1 < N and not visit[cafes[x+1][y-1]]:
            new_visit = visit[:]
            new_visit[cafes[x + 1][y - 1]] = True
            desert_tour(x + 1, y - 1, 1, new_visit, cnt+1)
        if 0 <= x - 1 < N and 0 <= y - 1 < N and not visit[cafes[x-1][y-1]]:
            new_visit = visit[:]
            new_visit[cafes[x - 1][y - 1]] = True
            desert_tour(x - 1, y - 1, 2, new_visit, cnt+1)
    # 진행방향이 ↖ 일때는, ↖ 또는 ↗로 진행할 수 있습니다.
    elif delta == 2:
        if 0 <= x - 1 < N and 0 <= y - 1 < N and not visit[cafes[x-1][y-1]]:
            new_visit = visit[:]
            new_visit[cafes[x - 1][y - 1]] = True
            desert_tour(x - 1, y - 1, 2, new_visit, cnt+1)
        if 0 <= x - 1 < N and 0 <= y + 1 < N and not visit[cafes[x-1][y+1]]:
            new_visit = visit[:]
            new_visit[cafes[x - 1][y + 1]] = True
            desert_tour(x - 1, y + 1, 3, new_visit, cnt+1)
    # 진행방향이 ↗ 일때는, ↗로만 진행할 수 있습니다.
    elif delta == 3:
        if 0 <= x - 1 < N and 0 <= y + 1 < N and not visit[cafes[x-1][y+1]]:
            new_visit = visit[:]
            new_visit[cafes[x - 1][y + 1]] = True
            desert_tour(x - 1, y + 1, 3, new_visit, cnt+1)


T = int(input())
for test_case in range(1, T+1):
    N = int(input())

    # 디저트의 종류 값을 저장할 2차원 배열 입니다.
    cafes = []
    for n in range(N):
        cafes += [list(map(int, input().split()))]

    # 만약 문제에서 주어진 조건을 만족하는 경우의 수가 없다면 -1을 출력하도록, 최대값을 -1로 시작합니다.
    MAXIMUM = -1

    # 이미 맛본 디저트의 종류값을 저장할 visit리스트의 원본입니다.
    V = [False for _ in range(101)]

    for i in range(N):
        for j in range(N):
            # 각각의 칸마다 매번 초기화해줘야 하므로 원본에서 복사하여 초기화해줍니다.
            visit = V[:]
            # 시작하는 칸의 디저트 값을 방문표시 해줍니다.
            visit[cafes[i][j]] = True
            # 만약 ↘로 진행할 수 있다면
            if 0 <= i + 1 < N and 0 <= j + 1 < N and not visit[cafes[i+1][j+1]]:
                # 방문표시 해주고, 위 함수를 실행합니다.
                visit[cafes[i+1][j+1]] = True
                desert_tour(i+1, j+1, 0, visit)

    print("#{} {}".format(test_case, MAXIMUM))
