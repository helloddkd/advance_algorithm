import sys
from collections import deque
sys.stdin = open('1949.txt','r')

T = int(input())

dix = [0, 0, 1, -1]
diy = [1, -1, 0, 0]

# DFS방식으로 등산로를 뚫어나가면서 만약 산하나를 만나면 k를 false로 만들고 다시뚫어나간다.
def DFS(start, k=True, result=1):
    global arr
    global max_result
    x, y = start[0], start[1]
    # 왔던곳을 다시오면 안되므로 visited 를 사용한다.
    visited[y][x] = True
    for di in range(4):
        new_x, new_y = x + dix[di], y + diy[di]
        if new_x < 0 or new_x > N - 1 or new_y < 0 or new_y > N - 1:
            continue
        if arr[y][x] > arr[new_y][new_x] and visited[new_y][new_x] == False:
            DFS((new_x, new_y), k, result + 1)
            visited[new_y][new_x] = False
        if arr[y][x] <= arr[new_y][new_x] and visited[new_y][new_x] == False:
            if k and arr[new_y][new_x] - arr[y][x] < K:
                temp = arr[new_y][new_x]
                arr[new_y][new_x] = arr[y][x] - 1
                k = False
                DFS((new_x, new_y), k, result + 1)
                k = True
                visited[new_y][new_x] = False
                arr[new_y][new_x] = temp
            elif k == False:
                continue
    else:
        if max_result < result:
            max_result = result
    visited[y][x] = False


for _ in range(T):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for __ in range(N)]
    top = max(map(max, arr))
    start = []
    max_result = 1
    visited = [[False] * N for ___ in range(N)]
    for iy in range(N):
        for ix in range(N):
            if arr[iy][ix] == top:
                start.append((ix, iy))
    for now in start:
        DFS(now)
    print('#{} {}'.format(_ + 1, max_result))
