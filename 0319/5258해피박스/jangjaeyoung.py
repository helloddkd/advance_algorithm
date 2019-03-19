import sys

sys.stdin = open('5258.txt', 'r')

T = int(input())
for test_case in range(1, T+1):
    N, M = tuple(map(int, input().split()))

    items = []
    for i in range(M):
        items.append(list(map(int, input().split())))

    result = 0
    for i in range(2 ** M):
        temp_result = 0
        temp_sum = 0
        for j in range(M):
            if i & (1 << j):
                if temp_sum + items[M-1-j][0] <= N:
                    temp_result += items[M-1-j][1]
                    temp_sum += items[M-1-j][0]
                else:
                    break

        if temp_result > result:
            result = temp_result

    print('#{} {}'.format(test_case, result))
