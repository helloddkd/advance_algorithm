import sys
sys.stdin = open('B13458.txt', 'r')


N = int(input())
arr = list(map(int, input().split()))
B,C = map(int, input().split())
re = N
for j in range(len(arr)):
    arr[j] -= B
    if arr[j] > 0:
        t = arr[j]//C
        re += t
        r = arr[j]%C
        if r:
            re += 1
print(re)

#꼭 기억하기!!! 음수여도 divmod 돌아간다는거,,
