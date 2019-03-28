import sys
from copy import deepcopy
from collections import deque
sys.stdin = open('BJ12100.txt')

def function_2048(n):
    global Max
    direction = ['up', 'down', 'left', 'right']
    if n == 5:
        Max = max(Max, change(stack))
        return Max
    for dir in direction:
        stack.append(dir)
        function_2048(n + 1)
        stack.pop()

def change(stack):
    MAP = deepcopy(board)
    for direction in stack:
        nums1 = deque()
        if direction == 'up':
            for j in range(N):
                for i in range(N):
                    if MAP[i][j] != 0:
                        nums1.append(MAP[i][j])
                nums2 = fill(nums1)
                for i in range(N):
                    if len(nums2):
                        MAP[i][j] = nums2.popleft()
                    else:
                        MAP[i][j] = 0
        elif direction == 'down':
            for j in range(N):
                for i in range(1, N + 1):
                    if MAP[-i][j] != 0:
                        nums1.append(MAP[-i][j])
                nums2 = fill(nums1)
                for i in range(1, N + 1):
                    if len(nums2):
                        MAP[-i][j] = nums2.popleft()
                    else:
                        MAP[-i][j] = 0
        elif direction == 'left':
            for i in range(N):
                for j in range(N):
                    if MAP[i][j] != 0:
                        nums1.append(MAP[i][j])
                nums2 = fill(nums1)
                for j in range(N):
                    if len(nums2):
                        MAP[i][j] = nums2.popleft()
                    else:
                        MAP[i][j] = 0
        elif direction == 'right':
            for i in range(N):
                for j in range(1, N + 1):
                    if MAP[i][-j] != 0:
                        nums1.append(MAP[i][-j])
                nums2 = fill(nums1)
                for j in range(1, N + 1):
                    if len(nums2):
                        MAP[i][-j] = nums2.popleft()
                    else:
                        MAP[i][-j] = 0

    Max = 0
    for li in MAP:
        Max = max(Max, max(li))
    return Max

def fill(nums1):
    nums2 = deque()
    while len(nums1):
        if len(nums1) == 1:
            nums2.append(nums1.popleft())
        else:
            a = nums1.popleft()
            b = nums1[0]
            if a == b:
                nums2.append(a + b)
                nums1.popleft()
            else:
                nums2.append(a)
    return nums2


N = int(input())
board, stack = [], []
Max = 0
count = 0
for i in range(N):
    board.append(list(map(int, input().split())))
function_2048(0)
print(Max)

