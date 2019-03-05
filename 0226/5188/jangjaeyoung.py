import sys

sys.stdin = open('5188.txt', 'r')


def calculate_min_sum(x, y, acc_total):
    global min_sum
    if x + y == (N-1) * 2:
        new_acc_total = acc_total + matrix[x][y]
        if new_acc_total < min_sum:
            min_sum = new_acc_total

        return

    new_acc_total = acc_total + matrix[x][y]
    if x + 1 < N and new_acc_total < min_sum:
        calculate_min_sum(x+1, y, new_acc_total)

    if y + 1 < N and new_acc_total < min_sum:
        calculate_min_sum(x, y+1, new_acc_total)


T = int(input())
for test_case in range(1, T+1):
    N = int(input())

    matrix = []
    for _ in range(N):
        matrix.append(list(map(int, input().split())))

    min_sum = (N-1) * 2 * 13
    calculate_min_sum(0, 0, 0)
    print('#{} {}'.format(test_case, min_sum))
