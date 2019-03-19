import sys
sys.stdin = open("5252.txt", "r")

T = int(input())
for t in range(1, T+1):

    # A 단어의 갯수 N 과 B 단어의 갯수 M

    N, M = map(int, input().split())
    A = []
    B = []

    # 공통으로 가지고 있는 단어의 수를 나타낼 변수 count

    count = 0

    # A 단어장
    for n in range(N):
        A += [input()]

    # B단어장
    for m in range(M):
        string = input()

        # 해당 단어가 A단어장에도 있다면 count를 1 더해준다.

        if string in A:
            count += 1

    print("#{} {}".format(t, count))