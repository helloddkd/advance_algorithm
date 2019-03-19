import sys

sys.stdin = open('5262.txt', 'r')


T = int(input())
for test_case in range(1, T+1):
    information = list(map(int, input().split()))

    N = information[0]
    numbers = information[1:]

    D = [1 for _ in range(information[0])]

    for i in range(1, N):
        for j in range(i):
            if numbers[j] < numbers[i]:
                if D[i] <= D[j]:
                    D[i] = D[j] + 1

    result = max(D)

    print('#{} {}'.format(test_case, result))
