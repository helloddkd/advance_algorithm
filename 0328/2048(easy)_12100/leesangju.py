from copy import deepcopy
import sys
sys.stdin = open("acm_12100.txt", "r")

# 각각의 방향으로 2차원배열을 정리하는 함수를 만들었습니다.
def move_left(new_board):
    # for문 대신에 while문을 사용하였습니다.
    I = 0
    while I < N:
        J = 0
        while J < N:
            # 만약 해당 위치의 값이 0보다 크다면
            if new_board[I][J] > 0:
                # 다음에 나오는 수에 0보다 큰 값이 있고, 해당값과 더할 수 있다면, 원래 수에 더해주고 그 자리에 0을 넣습니다.
                K = J + 1
                while K < N:
                    if new_board[I][K] > 0 and new_board[I][K] == new_board[I][J]:
                        new_board[I][J], new_board[I][K] = new_board[I][J] * 2, 0
                        break
                    elif new_board[I][K] > 0 and new_board[I][K] != new_board[I][J]:
                        break
                    K += 1
            # 0이라면 0이 아닌 값을 끌어옵니다.
            else:
                K = J + 1
                while K < N:
                    if new_board[I][K] > 0:
                        new_board[I][J], new_board[I][K] = new_board[I][K], 0
                        break
                    K += 1
                # 끌어온 후 더할 수 있는 값이 있는지 찾아봅니다. 존재하는 경우 위와 동일한 과정을 거칩니다.
                P = J + 1
                while P < N:
                    if new_board[I][P] > 0 and new_board[I][P] == new_board[I][J]:
                        new_board[I][J], new_board[I][P] = new_board[I][J] * 2, 0
                        break
                    elif new_board[I][P] > 0 and new_board[I][P] != new_board[I][J]:
                        break
                    P += 1
            J += 1
        I += 1
    return new_board


def move_right(new_board):
    I = 0
    while I < N:
        J = N - 1
        while J >= 0:
            if new_board[I][J] > 0:
                K = J - 1
                while K >= 0:
                    if new_board[I][K] > 0 and new_board[I][K] == new_board[I][J]:
                        new_board[I][J], new_board[I][K] = new_board[I][J] * 2, 0
                        break
                    elif new_board[I][K] > 0 and new_board[I][K] != new_board[I][J]:
                        break
                    K -= 1
            else:
                K = J - 1
                while K >= 0:
                    if new_board[I][K] > 0:
                        new_board[I][J], new_board[I][K] = new_board[I][K], 0
                        break
                    K -= 1
                P = J - 1
                while P >= 0:
                    if new_board[I][P] > 0 and new_board[I][P] == new_board[I][J]:
                        new_board[I][J], new_board[I][P] = new_board[I][J] * 2, 0
                        break
                    elif new_board[I][P] > 0 and new_board[I][P] != new_board[I][J]:
                        break
                    P -= 1
            J -= 1
        I += 1
    return new_board


def move_down(new_board):
    I = 0
    while I < N:
        J = N - 1
        while J >= 0:
            if new_board[J][I] > 0:
                K = J - 1
                while K >= 0:
                    if new_board[K][I] > 0 and new_board[K][I] == new_board[J][I]:
                        new_board[J][I], new_board[K][I] = new_board[J][I] * 2, 0
                        break
                    elif new_board[K][I] > 0 and new_board[K][I] != new_board[J][I]:
                        break
                    K -= 1
            else:
                K = J - 1
                while K >= 0:
                    if new_board[K][I] > 0:
                        new_board[J][I], new_board[K][I] = new_board[K][I], 0
                        break
                    K -= 1
                P = J - 1
                while P >= 0:
                    if new_board[P][I] > 0 and new_board[P][I] == new_board[J][I]:
                        new_board[J][I], new_board[P][I] = new_board[J][I] * 2, 0
                        break
                    elif new_board[P][I] > 0 and new_board[P][I] != new_board[J][I]:
                        break
                    P -= 1
            J -= 1
        I += 1
    return new_board


def move_up(new_board):
    I = 0
    while I < N:
        J = 0
        while J < N:
            if new_board[J][I] > 0:
                K = J + 1
                while K < N:
                    if new_board[K][I] > 0 and new_board[K][I] == new_board[J][I]:
                        new_board[J][I], new_board[K][I] = new_board[J][I] * 2, 0
                        break
                    elif new_board[K][I] > 0 and new_board[K][I] != new_board[J][I]:
                        break
                    K += 1
            else:
                K = J + 1
                while K < N:
                    if new_board[K][I] > 0:
                        new_board[J][I], new_board[K][I] = new_board[K][I], 0
                        break
                    K += 1
                P = J + 1
                while P < N:
                    if new_board[P][I] > 0 and new_board[P][I] == new_board[J][I]:
                        new_board[J][I], new_board[P][I] = new_board[J][I] * 2, 0
                        break
                    elif new_board[P][I] > 0 and new_board[P][I] != new_board[J][I]:
                        break
                    P += 1
            J += 1
        I += 1
    return new_board


def find_answer(arr, k):
    global MAX
    # 5번을 돌립니다. 그냥 arr을 쓸 경우 그 2차원배열이 유지되어 값이 누적되어 답이 안나와서 deepcopy로 계속 초기화해줍니다.
    if k == 5:
        for LIST in arr:
            if max(LIST) > MAX:
                MAX = max(LIST)
        return
    find_answer(move_up(deepcopy(arr)), k + 1)
    find_answer(move_down(deepcopy(arr)), k + 1)
    find_answer(move_left(deepcopy(arr)), k + 1)
    find_answer(move_right(deepcopy(arr)), k + 1)

N = int(input())

arr = []
for n in range(N):
    arr += [list(map(int, input().split()))]

MAX = 0

find_answer(arr, 0)
print(MAX)
