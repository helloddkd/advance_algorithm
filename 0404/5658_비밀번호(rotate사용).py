from collections import deque
import sys
sys.stdin = open("5658.txt", "r")

# 덱의 함수 rotate를 사용해보았습니다.

T = int(input())
for test_case in range(1, T+1):
    N, K = map(int, input().split())

    # 16진수 문자열의 원본입니다.
    password = input()

    # 해당 문자열을 덱에 옮겨줍니다.
    PW = deque()
    for char in password:
        PW.append(char)

    # 결과값을 저장할 set입니다. 중복을 피하기 위해 list대신 set을 사용했습니다.
    num_set = set()

    # 전체를 4로 나누면 한 변에 있는 문자의 수가 나옵니다. 해당 문자수 만큼 배열의 위치를 변환해야하므로 for문을 돌렸습니다.
    for i in range(N//4):
        # 계속 원래 덱을 재사용해야하므로 카피를 만들었습니다.
        PW_copy = PW.copy()
        for j in range(4):
            # string 변수에 문자들을 추가합니다. j 반복문은 한 변을 뜻합니다.
            string = ""
            # 해당 변에 있는 문자의 수만큼 추가해줍니다.
            for z in range(N//4):
                Q = PW_copy.popleft()
                string += Q
            # 16진수 문자열을 10진수 숫자로 변환하여 set에 추가해줍니다.
            num_set.add((int(string, 16)))
        # 한칸씩 밀어줍니다.
        PW.rotate(-1)
    # 정렬을 위해 리스트로 변환합니다.
    num_list = list(num_set)
    num_list.sort(reverse=True)

    print("#{} {}".format(test_case, num_list[K-1]))