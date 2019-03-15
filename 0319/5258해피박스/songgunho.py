import sys
sys.stdin = open('5258.txt', 'r')

def happybox(a,b):
    if b == 0 and a < arr[b][0]:
        memorize[(a,b)] = 0
        return 0
    if b == 0 and a >= arr[b][0]:
        memorize[(a,b)] = arr[b][1]
        return arr[b][1]

    if (a,b) in memorize:
        return memorize[(a,b)]
    else:
        if a-arr[b][0] >= 0:
            result = max(happybox(a,b-1), arr[b][1] + happybox(a-arr[b][0],b-1))
        else:
            result = happybox(a,b-1)
        memorize[(a,b)] = result
        return result

T = int(input())
for _ in range(T):
    memorize = {}
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for __ in range(M)]
    # print('#{} {}'.format(_+1,result))
    happybox(N,M-1)
    result = memorize[N,M-1]
    print('#{} {}'.format(_+1,result))
