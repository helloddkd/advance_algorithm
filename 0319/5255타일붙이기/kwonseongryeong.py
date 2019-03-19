import sys
sys.stdin = open('5255.txt')


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    result = 0
    memo = [0, 1, 3, 6]
    for i in range(4, N + 1):
        memo.append(memo[-1] + 2*memo[-2] + memo[-3])

    print('#{} {}'.format(test_case, memo[N]))
