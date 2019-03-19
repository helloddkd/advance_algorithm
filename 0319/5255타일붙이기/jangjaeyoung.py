import sys

sys.stdin = open('5255.txt', 'r')


# def tile(N):
#     global result
#     if N == 1:
#         return result[1]
#     elif N == 2:
#         return result[2]
#     elif N == 3:
#         return result[3]
#     elif N > 3 and result[N] == 0:
#         result[N] = tile(N-3) + 2 * tile(N-2) + tile(N-1)
#
#     return result[N]


result = [0] * 31
result[1] = 1
result[2] = 3
result[3] = 6
for i in range(4, 31):
    result[i] = result[i-3] + 2 * result[i-2] + result[i-1]

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    print('#{} {}'.format(test_case, result[N]))
