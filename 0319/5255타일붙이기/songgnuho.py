import sys
sys.stdin = open('5255.txt', 'r')

memorize = {1:1, 2:3, 3:6}

def gazisoo(N):
    if N in memorize:
        return memorize[N]
    else:
        a1 = 1*gazisoo(N-3)
        a2 = 2*gazisoo(N-2)
        a3 = gazisoo(N-1)
        memorize[N] = a1+a2+a3
        return a1+a2+a3

T = int(input())
for _ in range(T):
    N = int(input())
    gazisoo(N)
    result = memorize[N]
    print('#{} {}'.format(_+1,result))