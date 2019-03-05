import sys
sys.stdin = open('5185.txt', 'r')

hexa = ['A', 'B', 'C', 'D', 'E', 'F']
num = [10, 11, 12, 13, 14, 15]

def find(arr, target):
    for z in range(len(arr)):
        if arr[z] == target:
            return True
    else:
        return False


def index(arr, target):
    for z in range(len(arr)):
        if arr[z] == target:
            return z
    else:
        return False

T = int(input())
for test in range(T):
    N, F = list(input().split())
    N = int(N)
    F = list(F)
    arr = ''
    for i in range(N):
        if find(hexa, F[i]):
            F[i] = num[index(hexa, F[i])]
        f = int(F[i])
        for k in range(3, -1, -1):
            arr += str(f//2**k)
            f = f % 2 ** k
    print(f'#{test+1} {arr}')