import sys
sys.stdin = open("5262.txt", "r")

# 강의에서 나온 방법을 사용, 동적으로 구함
for test_case in range(1, int(input())+1):

    # 자연수를 저장한 arr
    arr = list(map(int, input().split()))

    # 해당 위치에서 가능한 오름차순조합의 원소 갯수를 저장하는 리스트
    LIS = [0 for _ in range(len(arr)+1)]

    for i in range(1, len(arr)):

        # 해당 위치에 있는 자연수
        LIS[i] = 1

        # 그 전 중에서 해당 위치에 있는 자연수보다 작으면서, 원소 갯수가 많은 조합을 선택
        for j in range(1, i):
            if arr[j] < arr[i] and 1 + LIS[j] > LIS[i]:
                LIS[i] = 1 + LIS[j]

    print("#{} {}".format(test_case, max(LIS)))














