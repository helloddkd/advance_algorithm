import sys
sys.stdin = open('5258.txt')

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    goods = []
    Max = 0

    for i in range(M):
        goods.append(list(map(int, input().split())))

    for i in range(1 << M):
        weight = 0
        price = 0
        for j in range(M):
            if i & (1 << j):
                weight += goods[j][0]
                price += goods[j][1]
                if weight > N:
                    break
            if price > Max:
                Max = price

    print('#{} {}'.format(test_case, Max))