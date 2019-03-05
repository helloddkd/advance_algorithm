import sys

sys.stdin = open('5201.txt', 'r')

T = int(input())

for test_case in range(1, T+1):
    N, M = tuple(map(int, input().split()))
    containers = list(map(int, input().split()))
    capacities = list(map(int, input().split()))

    containers.sort(reverse=True)
    capacities.sort(reverse=True)

    result = 0
    for capacity in capacities:
        flag = False
        for container in containers:
            if capacity >= container:
                result += container
                flag = True
                temp = container
                break

        if flag:
            containers.remove(container)

    print(f'#{test_case} {result}')
