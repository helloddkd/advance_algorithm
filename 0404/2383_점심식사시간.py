import sys
sys.stdin = open("2383.txt", "r")


# 해당 층에 있는 사람들을 순열을 사용해서, 각각의 계단으로 가는 경우의 수를 모두 구했습니다.
# 그리고 나온 케이스들을 아래 count_time 함수로 보낸 후 시간을 계산해주었습니다.
def perm(k, n, case=0):
    global cases, MINIMUM

    # 사람 수 만큼 순열에 구성요소를 추가했다면 이제 해당 케이스를 시간을 구하는 함수로 넘겨줍니다.
    if k == n:
        temp = count_time(case)
        if temp < MINIMUM:
            MINIMUM = temp
        return

    # 한쪽 계단으로 가고 안가고를 비트연산자를 이용하여 표현합니다.
    perm(k+1, n, case | 1 << k)
    perm(k+1, n, case)


# 각각의 케이스에 걸리는 시간을 구하는 함수입니다. 시간을 리턴해줍니다.
def count_time(case):
    # 각 계단에 가는 사람들을 저장할 리스트 입니다.
    stair_1, stair_2 = [], []

    # 인덱스 만큼 비트 연산자를 왼쪽으로 이동하였을 때, 나오는 결과값이 1이냐 0이냐에 따라 다른 계단에 저장합니다.
    for person_idx in range(len(people)):
        if case & 1 << person_idx:
            # 사람과 계단 사이의 거리와 도착하고 내려가기 시작하기 까지 걸리는 시간 1을 더한 값을 리스트에 추가해줍니다.
            stair_1.append(abs(stairs[0][1] - people[person_idx][0]) + abs(stairs[0][2] - people[person_idx][1]) + 1)
        else:
            stair_2.append(abs(stairs[1][1] - people[person_idx][0]) + abs(stairs[1][2] - people[person_idx][1]) + 1)

    # 거리가 가까운 사람부터 표시되도록 오름차순으로 정리해주었습니다.
    stair_1.sort(); stair_2.sort()

    # 1번 계단에서 소요되는 단위시간을 저장할 변수입니다.
    cnt_1 = 0

    # 사람이 모두 계단에서 빠져나올때까지 이므로, while문을 사용하였습니다.
    while len(stair_1):
        # 반복문이 한 바퀴 돌때마다 단위시간을 1 더해줍니다.
        cnt_1 += 1
        # 3명까지 한번에 계단을 내려갈 수 있으므로 2번째(3번)까지만 0이하로 빼주고, 나머지는 0까지만 빼줍니다.
        for idx in range(len(stair_1)):
            if idx <= 2:
                stair_1[idx] -= 1
            elif idx > 2 and stair_1[idx] > 0:
                stair_1[idx] -= 1
        # 계단을 모두 내려운 사람은 쭉 빼줍니다.
        while len(stair_1) > 0 and stair_1[0] == -stairs[0][0]:
            stair_1.pop(0)

    # 2번 계단에서 소요되는 단위시간을 저장할 변수입니다.
    cnt_2 = 0
    while len(stair_2):
        cnt_2 += 1
        for idx in range(len(stair_2)):
            if idx <= 2:
                stair_2[idx] -= 1
            elif idx > 2 and stair_2[idx] > 0:
                stair_2[idx] -= 1
        while len(stair_2) > 0 and stair_2[0] == -stairs[1][0]:
            stair_2.pop(0)
    return max(cnt_1, cnt_2)


T = int(input())
for test_case in range(1, T+1):
    N = int(input())

    # 사람의 위치와 계단의 위치, 계단을 내려가는데 걸리는 시간을 저장할 2차원배열
    arr = []
    for n in range(N):
        arr += [list(map(int, input().split()))]

    # 사람의 위치와 계단의 위치, 필요시간을 저장할 리스트 입니다.
    people = []
    stairs = []
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                people.append((i, j))
            elif arr[i][j] > 1:
                stairs.append((arr[i][j], i, j))

    cases = []
    # 최소값은 최대한 크게 주었습니다.
    MINIMUM = 0xffffff
    # 0이 1씩 더해져서, 사람수만큼 반복됩니다.
    perm(0, len(people))
    print("#{} {}".format(test_case, MINIMUM))

