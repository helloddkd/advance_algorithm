import sys
sys.stdin = open('5262.txt')

T = int(input())
for test_case in range(1, T + 1):
    N = list(map(int, input().split()))
    N, nums = N[0], N[1:]
    Max = 0

    for i in range(1 << N):
        subset = []
        for j in range(N):
            if i & (1 << j):
                if len(subset) > 0 and subset[-1] > nums[j]:
                    break
                subset.append(nums[j])

        else:
            if len(subset) > Max:
                Max = len(subset)

    print('#{} {}'.format(test_case, Max))