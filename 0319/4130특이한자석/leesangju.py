import sys
sys.stdin = open("4130.txt", "r")

# 회전하는 자석의 왼쪽을 확인하는 함수
def left_side(magnet, spin):
    global M_start
    if magnet - 1 < 0:
        return
    else:
        # 만약 맞닿아 있는 자석의 극성이 다를 경우(인덱싱 에러 방지를 위해 나머지로 해준다)
        if magnets[magnet][(M_start[magnet] - 2) % 8] != magnets[magnet-1][(M_start[magnet - 1] + 2) % 8]:

            # 만약 반시계 회전이라면 닿아있는 자석이 시계방향으로 회전하므로 해당 자석의 시작위치를 -1, 뒤로 하나 해준다.
            if spin == -1:

                # 다음 자석의 경우 회전방향을 바꿔준다.
                left_side(magnet - 1, spin * (-1))

                # 바로 바꾸면 값이 틀려지므로 나중에 한번에 바뀌어 지도록 함수 뒤에 변경하는 코드를 넣는다.
                M_start[magnet-1] = M_start[magnet-1] - 1
            else:
                left_side(magnet - 1, spin * (-1))
                M_start[magnet - 1] = M_start[magnet - 1] + 1
        else:
            return

# 회전하는 자석의 오른쪽을 확인하는 함수
def right_side(magnet, spin):
    global M_start
    if magnet + 1 >= 4:
        return
    else:
        if magnets[magnet][(M_start[magnet] + 2) % 8] != magnets[magnet+1][(M_start[magnet+1] - 2) % 8]:
            if spin == -1:
                right_side(magnet + 1, spin * (-1))
                M_start[magnet+1] = M_start[magnet+1] - 1
            else:
                right_side(magnet + 1, spin * (-1))
                M_start[magnet + 1] = M_start[magnet + 1] + 1
        else:
            return


for test_case in range(1, int(input())+1):
    K = int(input())

    # 각 자석들의 N극, S극 분포 순서를 저장하는 리스트
    magnets = []
    for n in range(4):
        magnets += [list(map(int, input().split()))]

    # 각 자석의 시작 위치(화살표 위치)
    M_start = [0, 0, 0, 0]

    # 돌리기 시작
    for k in range(K):
        M, S = map(int, input().split())

        left_side(M-1, S)
        right_side(M-1, S)

        # 해당 자석을 돌려준다
        if S == -1:
            M_start[M-1] = M_start[M-1] + 1
        else:
            M_start[M-1] = M_start[M-1] - 1

    # 점수를 저장할 변수
    total_point = 0

    # 점수 규칙에 따라 더해준다. 인덱싱 에러 방지를 위해 나머지로 해준다.
    for idx in range(4):
        if magnets[idx][(M_start[idx]) % 8] == 1:
            total_point += 2**idx

    print("#{} {}".format(test_case, total_point))
