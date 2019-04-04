import sys
sys.stdin = open("5650.txt", "r")

# 2차원 배열을 만들어서 첫번째 칸부터 상하좌우로 쭉 진행하며 공이 벽을 만나거나 블록과 만나는 경우의 합의 최대값을 구했습니다.

# 델타를 사용하였습니다.
dxy = [[1, 0], [-1, 0], [0, 1], [0, -1]]

# 해당 작업을 수행하는 함수 입니다.
def play_pinball(a, b):

    # 최대값을 저장할 전역변수 MAXIMUM 입니다.
    global MAXIMUM

    # 상하좌우로 움직입니다.
    for delta in dxy:

        # 공이 벽을 만나거나 블록과 만날때 1을 더해줍니다.
        cnt = 0

        # a, b는 반복문이 끝나는 조건 중 하나이므로 바뀌면 안되니 새로 변수를 추가하였습니다.
        x, y = a, b

        dx, dy = delta[0], delta[1]

        # 쭉 더해야 하므로 for문 대신 while문을 사용하였습니다.
        while True:

            # 핀볼이 이동한 좌표입니다.
            x, y = x + dx, y + dy

            # 만약 벽과 만나지 않는다면
            if 0 <= x < N and 0 <= y < N:

                # 시작점과 만나면 반복문을 끝냅니다.
                if x == a and y == b:
                    break

                # 블랙홀을 만나면 반복문을 끝냅니다.
                elif arr[x][y] == -1:
                    break

                # 각각의 블록과 만났을 경우, 기존 진행 방향에 따라 새로운 방향이 결정되도록 해줍니다.
                elif arr[x][y] == 1:
                    if dx == 1:
                        dx, dy = 0, 1
                    elif dx == -1:
                        dx, dy = 1, 0
                    elif dy == 1:
                        dx, dy = 0, -1
                    elif dy == -1:
                        dx, dy = -1, 0
                    cnt += 1

                elif arr[x][y] == 2:
                    if dx == 1:
                        dx, dy = -1, 0
                    elif dx == -1:
                        dx, dy = 0, 1
                    elif dy == 1:
                        dx, dy = 0, -1
                    elif dy == -1:
                        dx, dy = 1, 0
                    cnt += 1

                elif arr[x][y] == 3:
                    if dx == 1:
                        dx, dy = -1, 0
                    elif dx == -1:
                        dx, dy = 0, -1
                    elif dy == 1:
                        dx, dy = 1, 0
                    elif dy == -1:
                        dx, dy = 0, 1
                    cnt += 1

                elif arr[x][y] == 4:
                    if dx == 1:
                        dx, dy = 0, -1
                    elif dx == -1:
                        dx, dy = 1, 0
                    elif dy == 1:
                        dx, dy = -1, 0
                    elif dy == -1:
                        dx, dy = 0, 1
                    cnt += 1

                elif arr[x][y] == 5:
                    if dx == 1:
                        dx, dy = -1, 0
                    elif dx == -1:
                        dx, dy = 1, 0
                    elif dy == 1:
                        dx, dy = 0, -1
                    elif dy == -1:
                        dx, dy = 0, 1
                    cnt += 1

                # 웜홀과 만났을 경우, 미리 웜홀의 위치를 저장한 리스트에서 현재 위치가 아닌 나머지 위치를 꺼내 x, y로 바꿔줍니다.
                elif arr[x][y] >= 6:
                    for warmhole in warmholes[arr[x][y]]:
                        if warmhole != (x, y):
                            x, y = warmhole[0], warmhole[1]
                            break

            # 만약 벽과 만난다면, 방향을 반대로 해주고, 쵯수를 1 더해줍니다.
            else:
                dx *= -1
                dy *= -1
                cnt += 1

        # 반복문이 끝나고, 튕긴 횟수가 기존 최대값 보다 크다면 그 값을 저장해줍니다.
        if cnt > MAXIMUM:
            MAXIMUM = cnt


T = int(input())
for test_case in range(1, T+1):

    N = int(input())
    arr = []
    for n in range(N):
        arr += [list(map(int, input().split()))]

    # 웜홀의 위치를 저장할 리스트입니다.
    warmholes = [[] for _ in range(11)]

    for i in range(N):
        for j in range(N):
            if arr[i][j] >= 6:
                warmholes[arr[i][j]] += [(i,j)]

    MAXIMUM = 0


    for i in range(N):
        for j in range(N):
            if arr[i][j] == 0:
                play_pinball(i, j)

    print("#{} {}".format(test_case, MAXIMUM))
