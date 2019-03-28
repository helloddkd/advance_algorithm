import sys
sys.stdin = open('14499.txt', 'r')

#동1 서2 북3 남4

N,M,x,y,K = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))
move = list(map(int, input().split()))
num_set = [{1,6}, {3,4}, {5,2}]
num = [1,6,3,4,5,2] #0 위 1 아래 2 동 3 서 4 남 5 북, 각 인덱스마다 주사위의 어떤 면이 바라보고 있는지 정함.
dice = [0]*7 #주사위의 각 면에 어떤 숫자가 쓰여 있는지 기록할 리스트
dice[6] = arr[x][y] #처음 시작할때는 6번 면이 바닥에 닿아 있으므로 0이 아니라 바닥면 숫자를 기록해줌.

for d in move:
    if d == 1:#동
        if y+1<M:
            y+=1
            num[1] = num[2] #(동서남북)으로 바꾸면 (동서남북)의 면이 아래로, 그리고 위의 면이 (동서남북)으로
            num[2] = num[0]
            num[0] = 7-num[1]
            num[3] = 7-num[2]#동서로 이동할 경우 남북은 변하지 않고, 남북으로 이동하면 동서를 바라보는 면은 변하지 않는다.
            if arr[x][y] == 0:
                arr[x][y] = dice[num[1]]
            else:
                dice[num[1]] = arr[x][y]
                arr[x][y] = 0
            print(dice[num[0]])
    elif d == 2:#서
        if 0<=y-1:
            y-=1
            num[1] = num[3]
            num[3] = num[0]
            num[0] = 7-num[1]
            num[2] = 7-num[3]
            if arr[x][y] == 0:
                arr[x][y] = dice[num[1]]
            else:
                dice[num[1]] = arr[x][y]
                arr[x][y] = 0
            print(dice[num[0]])
    elif d == 3: #북
        if 0<=x-1:
            x-=1
            num[1] = num[5]
            num[5] = num[0]
            num[0] = num[4]
            num[4] = 7-num[5]
            if arr[x][y] == 0:
                arr[x][y] = dice[num[1]]
            else:
                dice[num[1]] = arr[x][y]
                arr[x][y] = 0
            print(dice[num[0]])
    elif d == 4:
        if x+1<N:
            x+=1
            num[1] = num[4]
            num[4] = num[0]
            num[0] = num[5]
            num[5] = 7-num[4]
            if arr[x][y] == 0:
                arr[x][y] = dice[num[1]]
            else:
                dice[num[1]] = arr[x][y]
                arr[x][y] = 0
            print(dice[num[0]])