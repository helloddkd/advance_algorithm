import sys
sys.stdin = open('5208.txt', 'r')

T = int(input())
for test in range(1, T+1):
    arr = list(map(int, input().split()))
    N = arr[0]
    del(arr[0])
    arr.append(0)
    arr.insert(0,0)
    pos = N
    charge = 0

    while pos > 1:
        for i in range(len(arr)):
            if i + arr[i] >= pos:
                pos = i
                charge += 1
                break

    print(f'#{test} {charge-1}')