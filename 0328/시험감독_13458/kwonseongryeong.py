import sys
sys.stdin = open('BJ13458.txt')

for test_case in range(5):
    N = int(input())
    A = list(map(int, input().split()))
    B, C = map(int, input().split())
    count = 0
    for i in range(N):
        A[i] = A[i] - B
        count += 1
        if A[i] > 0:
            count += A[i] // C
        if A[i] > 0 and A[i] % C:
            count += 1
    print(count)
