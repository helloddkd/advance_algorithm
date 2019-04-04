import sys
from itertools import combinations, product

sys.stdin = open('2112.txt', 'r')


def check(film, cnt):
    # 약품을 한 번도 주입하지 않는 경우에 대해 조사합니다.
    if cnt == 0:
        # 필름을 열 단위로 탐색하면서 보호가 안되는 곳이 있는지 검사합니다.
        # 안 쪽의 for 문은 보호 기준이 충족되면 break 하고 다음 열로 이동하게 되어 있습니다.
        # 그리고 안쪽의 for 문이 기준을 만족하고 break로 끝났는지 아니면 그냥 끝까지 돌기만 해서 끝났는지 중간의 if 문으로 이를 검사합니다.
        # 즉 두 개의 for 문을 쭉 끝까지 통과하면 기준을 충족하는 것입니다.
        for j in range(W):
            acc = 0
            for i in range(D-1):
                if acc == K-1:
                    break

                if film[i][j] == film[i+1][j]:
                    acc += 1
                else:
                    acc = 0

            if acc != K-1:
                return False

        return True

    # 약품을 투입해야하는 경우를 조사합니다.
    # 약품을 투입하지 않는 경우와 거의 비슷합니다. 다만, 약품 검사를 하기 전에 조합을 사용해서 모든 경우에 대해 약품을 주입해가면서 검사를 한다는 점만 다릅니다.
    for combination in combinations(range(D), cnt):
        for prod in product(range(2), repeat=cnt):
            # 여러 번의 테스트를 위해 원본을 보존해야합니다. 그래서 테스트용 필름을 복사하고 진행합니다.
            test_film = [film[i][:] for i in range(D)]
            # 테스트 결과 기준이 충족된 조합이 나온다면 바로 빠져나와야 합니다.
            # 따라서 for 문이 어떻게 끝났는지 알기 위해서 flag 변수를 2개 사용했습니다.
            flag1 = False
            flag2 = False
            iter_cnt = 0
            for i in combination:
                test_film[i] = [prod[iter_cnt]] * W
                iter_cnt += 1

            for j in range(W):
                acc = 0
                for i in range(D - 1):
                    if acc == K - 1:
                        break

                    if test_film[i][j] == test_film[i + 1][j]:
                        acc += 1
                    else:
                        acc = 0

                if acc != K - 1:
                    flag1 = True
                    break
            else:
                flag2 = True

            if flag2:
                return True

            if flag1:
                continue


T = int(input())
for test_case in range(1, T+1):
    D, W, K = map(int, input().split())
    film = [list(map(int, input().split())) for _ in range(D)]

    cnt = 0
    result = check(film, cnt)
    if result:
        print('#{} {}'.format(test_case, cnt))
        continue

    cnt = 1
    while True:
        result = check(film, cnt)
        if result:
            break

        cnt += 1

    print('#{} {}'.format(test_case, cnt))
