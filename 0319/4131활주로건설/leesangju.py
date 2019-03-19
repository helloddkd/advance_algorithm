import sys
sys.stdin = open("4131.txt", "r")

T = int(input())
for test_case in range(1, T+1):

    # 행렬의 가로 세로 길이 N, 활주로의 길이 X

    N, X = map(int, input().split())
    arr = []
    for n in range(N):
        arr += [list(map(int, input().split()))]

    # 활주로 설치 여부를 확인할 2차원 리스트, 기본값 False로 설치시 True로 바뀐다. 각각 가로 오르막 내리막 / 세로 오르막 내리막

    changed_row_left = [[False for _ in range(N)] for _ in range(N)]
    changed_row_right = [[False for _ in range(N)] for _ in range(N)]
    changed_column_up =[[False for _ in range(N)] for _ in range(N)]
    changed_column_down = [[False for _ in range(N)] for _ in range(N)]

    # 활주로 설치 가능한 줄 갯수 저장할 case

    case = 0

    # 가로와 세로를 나누어서 실행하였습니다.
    for i in range(N):
        for j in range(N):

            # P는 활주로 설치 가능 여부를 판단, 조건을 만족하지 못하면 0으로 바꿈
            P = 1

            # 인덱스 에러 방지용 범위 한정, ◁ 모양의 경사로를 설치, 맨 왼쪽에서 오른쪽으로
            if j+1 < N:

                # 만약 높이가 1이 날 경우
                if arr[i][j+1] - arr[i][j] == 1:

                    # 이미 활주로가 설치되어 있는 곳이라면 뾰족하게 되므로 break시키고 P를 0으로
                    if changed_row_right[i][j+1] == True:
                        P = 0
                        break
                    K = 0
                    cnt = 0

                    # 맨 왼쪽에 도달하거나 값이 달라지거나 경사면이 이미 설치된 곳을 만나면 끝나도록 while문 설정
                    while j - K >= 0 and arr[i][j-K] == arr[i][j] and not changed_row_right[i][j-K]:
                        cnt += 1
                        K += 1

                    # 같은 높이를 가진 길의 거리가 활주로의 길이보다 같거나 클 경우, 경사로 설치
                    if cnt >= X:
                        for x in range(X):
                            changed_row_left[i][j-x] = True

                    # 아니면 break
                    else:
                        P = 0
                        break

                # 높이차 2 이상이 날 경우 활주로 설치 불가, break하고 P를 0으로 바꿈
                elif abs(arr[i][j+1] - arr[i][j]) > 1:
                    P = 0
                    break

            # ▷ 모양의 경사로 설치는 맨 오른쪽에서 부터 왼쪽으로 진행
            if (N-1)-j-1 >= 0:
                if arr[i][(N-1)-j-1] - arr[i][(N-1)-j] == 1:
                    if changed_row_left[i][(N-1)-j-1] == True:
                        P = 0
                        break
                    K = 0
                    cnt = 0
                    while (N-1)-j + K < N and arr[i][(N-1)-j + K] == arr[i][(N-1)-j] and not changed_row_left[i][(N-1)-j + K]:
                        cnt += 1
                        K += 1
                    if cnt >= X:
                        for x in range(X):
                            changed_row_right[i][(N-1)-j + x] = True
                    else:
                        P = 0
                        break
                elif abs(arr[i][(N-1)-j-1] - arr[i][(N-1)-j]) > 1:
                    P = 0
                    break
        if P:
            case += 1

    for i in range(N):
        for j in range(N):
            P = 1

            if j+1 < N:
                if arr[j+1][i] - arr[j][i] == 1:
                    if changed_column_down[j+1][i] == True:
                        P = 0
                        break
                    K = 0
                    cnt = 0
                    while j - K >= 0 and arr[j-K][i] == arr[j][i] and not changed_column_down[j-K][i]:
                        cnt += 1
                        K += 1
                    if cnt >= X:
                        for x in range(X):
                            changed_column_up[j-x][i] = True
                    else:
                        P = 0
                        break
                elif abs(arr[j+1][i] - arr[j][i]) > 1:
                    P = 0
                    break


            if (N-1)-j-1 >= 0:
                if arr[(N-1)-j-1][i] - arr[(N-1)-j][i] == 1:
                    if changed_column_up[(N-1)-j-1][i] == True:
                        P = 0
                        break
                    K = 0
                    cnt = 0
                    while (N-1)-j + K < N and arr[(N-1)-j + K][i] == arr[(N-1)-j][i] and not changed_column_up[(N-1)-j + K][i]:
                        cnt += 1
                        K += 1
                    if cnt >= X:
                        for x in range(X):
                            changed_column_down[(N-1)-j + x][i] = True
                    else:
                        P = 0
                        break
                elif abs(arr[(N-1)-j-1][i] - arr[(N-1)-j][i]) > 1:
                    P = 0
                    break
        if P:
            case += 1

    print("#{} {}".format(test_case, case))