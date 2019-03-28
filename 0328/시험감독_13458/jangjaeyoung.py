import sys

sys.stdin = open('13458.txt', 'r')

N = int(input())
class_room = list(map(int, input().split()))
B, C = map(int, input().split())

cnt = 0
for i in class_room:
    i -= B
    cnt += 1
    if i <= 0:
        continue

    vice = i // C
    i = i % C
    if i == 0:
        cnt += vice
    else:
        cnt += vice + 1

print(cnt)
