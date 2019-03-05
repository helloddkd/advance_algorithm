import sys
sys.stdin = open('5201.txt', 'r')
T= int(input())
for test in range(T):
    N, M = list(map(int, input().split()))
    wi = sorted(list(map(int, input().split())), reverse=True)
    ti = sorted(list(map(int, input().split())), reverse=True)
    Sum = 0

    ww = [x for x in wi if x <= max(ti)]
    N = len(ww)
    for i in range(min(N, M)):
        if ti[i] >= ww[i]:
            Sum += ww[i]
    print(f'#{test+1} {Sum}')