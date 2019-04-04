import sys
sys.stdin = open('5658.txt')

T = int(input())
for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    data = list(input())
    convert = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
    n = N // 4      # 자물쇠는 정사각형 모양이므로 data를 4로 나누어 암호의 길이를 저장
    nums = {}       # key : 만들 수 있는 암호, value : key를 십진수로 변환한 값
    array = []      # 암호의 십진수 변환값을 저장하는 배열

    for k in range(n):  # n만큼 회전하면 만들 수 있는 암호를 모두 확인 할 수 있음
        for i in range(0, N, n):    # 암호의 길이만큼 점프하면서 for문을 돌림
            check = ''              # 암호를 저장할 변수
            for j in range(n):
                check += data[i + j]
            if check in nums:       # 암호가 nums에 있으면 continue
                continue
            num = 0
            for j in range(n):      # 암호를 십진수로 변환하는 for문
                if check[j] in convert:
                    num += convert[check[j]] * (16 ** (n - 1 - j))
                else:
                    num += int(check[j]) * (16 ** (n - 1 - j))
            nums[check] = num       # nums에 암호와 십진수 변환값을 저장함
            array.append(num)
        data.insert(0, data.pop())  # 시계방향으로 회전시켜줌
    array.sort(reverse=True)
    print('#{} {}'.format(test_case, array[K - 1]))