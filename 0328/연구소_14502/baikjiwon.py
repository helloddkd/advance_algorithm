import sys
sys.stdin = open('B14052.txt', 'r')

from copy import deepcopy
from collections import deque
from itertools import combinations

def countsafe():
    global Max
    count = 0
    for r in range(N):
        for c in range(M):
            if copy[r][c] == 0:
                count += 1
    Max = max(Max, count)
    return

def BFS():
    global copy
    virus = deepcopy(Virus)
    while virus:
        r,c = virus.popleft()
        for i in range(4):
            rr = r + dr[i]
            cc = c + dc[i]
            if 0<=rr<N and 0<=cc<M and copy[rr][cc]==0:
                copy[rr][cc] = 2
                virus.append([rr,cc])

N,M = map(int, input().split())
arr =[]
for _ in range(N):
    arr.append(list(map(int, input().split())))
Virus = deque()
Wall = []
dr = [0,0,1,-1]
dc = [-1,1,0,0]
Max = 0
for r in range(N):
    for c in range(M):
        if arr[r][c] == 2:#바이러스 위치기록
            Virus.append([r,c])
        elif arr[r][c] == 0:#0인 빈공간 위치 기록 -> 조합으로 3개 벽 어디세울지 찾기
            Wall.append([r,c])

for com in combinations(Wall,3):
        copy = deepcopy(arr) # 복사본 지도에다가 벽세우고 바이러스 퍼뜨려서 찾기
        for y,x in com:
            copy[y][x] = 1
        BFS()
        countsafe()
print(Max)




