import sys
sys.stdin = open("5255.txt", "r")


# 타일의 경우의 수를 tile 재귀 합수로 구한다

def tile(N):
    global count, memo
    if N <= 3:
        return memo[N]
    else:
        # 값이 저장되어 있다면 해당 값을 리턴한다(초기값이 0)
        if memo[N] != 0:
            return memo[N]
        else:
            # 현재위치 칸의 경우의 수 = 3칸 앞 경우의 수 + 2칸 앞 경우의 수 *2 + 1칸 앞 경우의 수
            memo[N] = tile(N-3) + tile(N-2)*2 + tile(N-1)
            return tile(N-3) + tile(N-2)*2 + tile(N-1)


T = int(input())
for test_case in range(1, T+1):
    N = int(input())

    # 경우의 수를 저장할 변수 count
    count = 0

    # memoization 해줄 memo
    memo = [ 0 for _ in range(N+1)]
    memo[0] = 1; memo[1] = 1; memo[2] = 3; memo[3] = 6;

    tile(N)

    print("#{} {}".format(test_case, memo[N]))



