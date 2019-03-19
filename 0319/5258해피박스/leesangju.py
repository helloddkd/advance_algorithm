import sys
sys.stdin = open("5258.txt", "r")


# select 재귀함수를 사용하여 가격 합계의 최대값을 구한다.
# start = 시작위치, value = 가격합계, weight = 무게 합계, N = 최대무게
def select(N, start, weight = 0, value = 0):

    # 상품의 정보를 저장한 arr 리스트와 최대값을 저장할 maximum
    global arr, maximum

    # start 값을 갱신해나가며 조건에 맞는 조합을 고르고, 최대값을 저장한다.
    for i in range(start, len(arr)):
        if weight + arr[i][0] <= N:
            if maximum < value + arr[i][1]:
                maximum = value + arr[i][1]
            select(N, i+1, weight + arr[i][0], value + arr[i][1])


T = int(input())
for test_case in range(1, T+1):

    # 최대무게 N, 상품 갯수 M
    N, M = map(int, input().split())
    arr = []
    maximum = 0
    for m in range(M):
        S, P = map(int, input().split())
        arr += [[S, P]]
    select(N, 0)
    print("#{} {}".format(test_case, maximum))