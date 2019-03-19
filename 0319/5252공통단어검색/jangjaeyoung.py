import sys

sys.stdin = open('5252.txt', 'r')

T = int(input())
for test_case in range(1, T+1):
    N, M = tuple(map(int, input().split()))

    A = [0] * N
    for i in range(N):
        A[i] = input()

    B = [0] * M
    for i in range(M):
        B[i] = input()

    cnt = 0
    B_copy = B[:]
    length_A = len(A)
    for i in range(length_A):
        length_B_copy = len(B_copy)
        flag = False
        for j in range(length_B_copy):
            if A[i] == B_copy[j]:
                cnt += 1
                flag = True
                temp = j
                break

        if flag:
            B_copy.pop(temp)

    print('#{} {}'.format(test_case, cnt))
