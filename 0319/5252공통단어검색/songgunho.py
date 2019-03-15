import sys
sys.stdin = open('5252.txt', 'r')

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    arrA = [input() for __ in range(N)]
    arrB = [input() for __ in range(M)]
    result = 0
    for i in range(N):
        if arrA[i] in arrB:
            result += 1

    print('#{} {}'.format(_+1, result))
