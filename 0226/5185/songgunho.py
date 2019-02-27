import sys

sys.stdin = open("5185.txt", "r")

a = list(map(str, range(10))) +['A', 'B', 'C', 'D', 'E', 'F']

Numb_test = int(input())
for _ in range(Numb_test):
    N, arr = list(input().split())
    sum_result = sum(a.index(arr[-i-1])*(16**i) for i in range(int(N)))
    result = bin(sum_result)[2:]
    rest = (4 - len(result)%4)%4
    result = '0'*rest + result 
    print(f'#{_+1} {result}')