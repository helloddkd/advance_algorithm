import sys

sys.stdin = open('5208.txt', 'r')

T = int(input())

for test_case in range(1, T+1):
    information = list(map(int, input().split()))

    N = information[0]
    i = 1
    count = 0
    while i < N:
        if i + information[i] < N:
            temp_max = 0
            for j in range(i+1, i+information[i]+1):
                temp = j + information[j]
                if temp > temp_max:
                    temp_max = temp
                    i = j

            count += 1
        else:
            break

    print(f'#{test_case} {count}')
