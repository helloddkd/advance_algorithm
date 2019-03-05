import sys
sys.stdin = open("5201.txt","r")

T = int(input())
for test_case in range(1,T+1):
    N, M = map(int, input().split())
    w = list(map(int, input().split()))
    t = list(map(int, input().split()))
    w.sort(reverse=True);t.sort(reverse=True)
    total_weight, j = 0, 0
    for i in range(N):
        if j == M:
            break
        if w[i] <= t[j]:
            total_weight += w[i]
            j += 1
    print(f"#{test_case} {total_weight}")