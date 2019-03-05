import sys
sys.stdin = open('5188.txt')


def min_search(x, y, Sum=0):
    global Min
    XY = [[x + 1, y], [x, y + 1]]
    Sum += nums[x][y]

    if x == N - 1 and y == N - 1:
        if Min > Sum:
            Min = Sum

    for xy in XY:
        if Sum > Min:
            break
        if xy[0] == N:
            continue
        if xy[1] == N:
            continue
        min_search(xy[0], xy[1], Sum)
    return Min


T = int(input())
for test_case in range(T):
    N = int(input())
    nums = []
    Min = (2*N - 1)*13

    for i in range(N):
        nums.append(list(map(int, input().split())))

    print('#{} {}'.format(test_case + 1, min_search(0, 0)))



