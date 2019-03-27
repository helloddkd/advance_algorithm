from collections import deque
from itertools import combinations
from copy import deepcopy
import sys
sys.stdin = open('ex.txt', 'r')

dix = [0,0,1,-1]
diy = [1,-1,0,0]

def BFS(start,Nair):
    global tempvisit, result
    que = deque()
    for __ in start:
        que.append(__)
    while que:
        x,y = que.popleft()
        for di in range(4):
            newx,newy = x-dix[di], y-diy[di]
            if 0<= newx < X and 0 <= newy < Y:
                if tempvisit[newy][newx] == False:
                    Nair -= 1
                    que.append((newx,newy))
                    tempvisit[newy][newx] = True
        if Nair <= result:
            return
    else:
        result = max(result,Nair)



Y, X = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(Y)]
visited = [[False]*X for _ in range(Y)]

result = 0

max_result = Y*X-3
start = []
air = []

for i in range(Y):
    for j in range(X):
        if arr[i][j] == 0:
            air.append((j,i))
        if arr[i][j] == 2:
            start.append((j,i))
            visited[i][j] = True
            max_result -= 1
        if arr[i][j] == 1:
            visited[i][j] = True
            max_result -= 1
# print(max_result)
# print(visited)
# print(start)

temp_index = combinations(range(len(air)),3)
for now in temp_index:
    tempvisit = deepcopy(visited)
    for t in now:
        tempvisit[air[t][1]][air[t][0]] = True
    BFS(start,max_result)

print(result)