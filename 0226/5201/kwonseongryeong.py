import sys
sys.stdin = open('5201.txt')

T = int(input())
for test_case in range(T):
    N, M = map(int, input().split())
    W = list(map(int, input().split()))
    T = list(map(int, input().split()))
    Sum, Max = 0, 1

    for i in range(M-1):
        Max = T[i]
        idx = i
        for j in range(i+1, M):
            if Max < T[j]:
                Max = T[j]
                idx = j
        T[idx], T[i] = T[i], T[idx]

    for i in range(M):
        weight_max = 0
        
        for j in range(len(W)):
            if (W[j] <= T[i]) and (W[j] > weight_max):
                weight_max = W[j]
                weight_idx = j
        if weight_max:
            Sum += weight_max
            W.pop(weight_idx)
            if len(W) == 0:
                break
        else:
            break

    print('#{} {}'.format(test_case + 1, Sum))


