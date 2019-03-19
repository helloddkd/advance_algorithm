import sys
sys.stdin = open('5252.txt')

T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    dictionary = {}
    count = 0

    for i in range(N + M):
        word = input()
        if word in dictionary:
            dictionary[word] += 1
        else:
            dictionary[word] = 1

    for key, value in dictionary.items():
        if value > 1:
            count += 1

    print('#{} {}'.format(test_case, count))
                     