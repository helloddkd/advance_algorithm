import sys

sys.stdin = open('5262.txt', 'r')

T = int(input())

for _ in range(T):
    arr = list(map(int, input().split()))
    dp = [1] * len(arr)
    for i in range(len(arr)):
        for j in range(i):
            if arr[i] > arr[j]:
                if dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1

    print('#{} {}'.format(_+1,max(dp)))

