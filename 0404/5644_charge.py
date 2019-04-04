import sys
sys.stdin = open('5644.txt')

def charging_station(index, X, Y, C):
    for i in range(X - C, X + C + 1):  # 충전 범위의 가운데 행을 먼저 저장
        if 0 <= i <= 9:
            MAP[Y][i].append(index)     # 지도에 충전기의 인덱스를 저장함
    for i in range(1, C + 1):           # 범위의 가운데를 기준으로 대칭이므로 아래 위를 한번에 저장
        for j in range(X - C + i, X + C + 1 - i):
            if 0 <= Y - i <= 9 and 0 <= j <= 9:
                MAP[Y - i][j].append(index)
            if 0 <= Y + i <= 9 and 0 <= j <= 9:
                MAP[Y + i][j].append(index)


# direction에 해당하는 위치로 움직임
def move(I, J, direction):
    locate = {0: [I, J], 1: [I - 1, J], 2: [I, J + 1], 3: [I + 1, J], 4: [I, J - 1]}
    return [locate[direction][0], locate[direction][1]]

T = int(input())
for test_case in range(1, T + 1):
    M, A = map(int, input().split())            # M : 충전기 개수, A : 움직임 횟수
    a_move = list(map(int, input().split()))    # a가 움직이는 인덱스
    b_move = list(map(int, input().split()))    # b가 움직이는 인덱스
    MAP = [[[] for _ in range(10)] for _ in range(10)]
    station = []    # 충전기의 성능을 저장하는 배열
    for i in range(A):
        X, Y, C, P = map(int, input().split())
        X, Y = X - 1, Y - 1     # 인덱스를 맞춰주기 위해 1씩 빼줌
        station.append(P)       # station에 성능을 저장하고
        charging_station(i, X, Y, C)    # 지도에 표시하러 갑시다

    result = 0
    a_location, b_location = [0, 0], [9, 9]
    for i in range(M + 1):
        Max = 0
        # a와 b가 도착한 지도의 위치에서 접근할 수 있는 충전기의 개수
        len_a = len(MAP[a_location[0]][a_location[1]])
        len_b = len(MAP[b_location[0]][b_location[1]])

        # a와 b가 둘 다 여러 충전기에 접속할 수 있는 경우
        if len_a > 0 and len_b > 0:
            # 같은 충전기를 제외하고 최대 충전양을 찾음
            for k in MAP[a_location[0]][a_location[1]]:
                for l in MAP[b_location[0]][b_location[1]]:
                    Sum = station[k]
                    if k != l:
                        Sum += station[l]
                    if Max < Sum:
                        Max = Sum
            result += Max

        # 한명씩만 충전할 수 있는 경우 접근할 수 있는 충전기에서 최대 값을 찾아서 더해줌
        elif len_a > 0 and len_b == 0:
            result += max(station[a] for a in MAP[a_location[0]][a_location[1]])
        elif len_b > 0 and len_a == 0:
            result += max(station[a] for a in MAP[b_location[0]][b_location[1]])
        if i == M:
            break

        # a와 b의 위치를 바꿔줌
        a_location = move(a_location[0], a_location[1], a_move[i])
        b_location = move(b_location[0], b_location[1], b_move[i])
    print('#{} {}'.format(test_case, result))