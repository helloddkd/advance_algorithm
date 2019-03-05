import sys
sys.stdin = open('5208.txt')


def electric_bus(stop, max_stop, count=0):
    global Min

    for i in range(1, max_stop+1):
        if stop + max_stop >= N[0]:
            if Min > count:
                Min = count
            break
        if count > Min:
            break
        electric_bus(stop+i, N[stop+i], count+1)
    return Min


T = int(input())
for test_case in range(T):
    N = list(map(int, input().split()))
    i, count = 1, 0
    Min, max_stop = N[0], N[i]

    electric_bus(i, N[i])
    print('#{} {}'.format(test_case + 1, Min))
