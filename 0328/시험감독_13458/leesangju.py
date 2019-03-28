import sys
sys.stdin = open("acm_13458.txt", "r")

N = int(input())

arr = list(map(int, input().split()))

# 총감독관, 부감독관이 담당할 수 있는 학생의 수를 받았습니다.
B, C = map(int, input().split())

SUM = 0

for n in range(N):
    # 총감독관이 담당할 수 있는 학생수보다 전체 학생수가 적다면 1만 더했습니다.
    if arr[n] - B <= 0:
        SUM += 1
    # 아니라면, 총감독관이 담당할 수 있는 학생수를 전체에서 빼고, C로 나눈 몫과 나머지를 이용하여 필요한 감독관의 수를 구했습니다.
    else:
        SUM += 1
        SUM += (arr[n]-B) // C
        if (arr[n]-B) % C:
            SUM += 1

print(SUM)