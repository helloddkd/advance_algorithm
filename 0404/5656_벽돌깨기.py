import sys
sys.stdin = open('5656.txt', 'r')

from collections import deque
def collide(r,c, arr, blocks):
    b = arr[r][c] #몇개의 구슬을 연달아 삭제해야 하는지 값을 잡아둠
    arr[r][c] = 0 #먼저 부딪힌 지점의 구슬을 깨서 0으로 만들어줌
    blocks -= 1 #총 블럭 개수에서 1을 뺀다.

    L = R = U = D = 1 #4방으로 구슬에 쓰여진 개수-1만큼 깬다.
    while L < b and W>c-L>=0:
        if arr[r][c - L] != 0:
            arr, blocks = collide(r, c-L, arr, blocks) #만약 깨지는 범위 안에 다른 구슬이 또 있으면 그 구슬도 깨준다.
        L += 1
    while R < b and 0<=c+R<W:
        if arr[r][c + R] != 0:
            arr, blocks = collide(r, c+R, arr, blocks)
        R += 1
    while U < b and 0<=r-U<H:
        if arr[r-U][c] != 0:
            arr, blocks = collide(r-U, c, arr, blocks)
        U += 1
    while D < b and 0<=r+D<H:
        if arr[r+D][c] != 0:
            arr, blocks = collide(r+D, c, arr, blocks)
        D += 1
    return arr, blocks

def makepermu(n=0, per = []):
    global Min
    if Min == 0: #이게 시간 줄이는 포인트!!!!!!!!!!!!!!!!!!!!!!!!! 이미 최소값 나왔으면 뒤는 쳐다보지말기
        return
    perr = per + [n]
    if len(perr) == N:
        arr = [Map[k][:] for k in range(H)]
        blocks = Blocks
        for i in range(N): #순열 각 원소에 있는 c인덱스에서 구슬을 떨어뜨린다
            for r in range(H):
                if arr[r][perr[i]] != 0:
                    arr, blocks = collide(r, perr[i], arr, blocks) #그때그때 맵상황이랑 남은 블럭개수를 리턴으로 받는다.
                    break
            #터뜨리고 나서 0을 정리해줘야함
            no = []
            for rr in range(H-1,-1,-1): #맨밑에줄부터 본다
                if len(no) == W:
                    break
                for cc in range(W):
                    if arr[rr][cc] == 0 and cc not in no: #밑줄부터 보다가 0이 있으면, 그 열의 윗줄들을 일렬로 살펴본다.
                        Q = deque()
                        for k in range(rr-1,-1,-1):
                            if arr[k][cc] != 0: #윗줄에서 0 아닌것을 덱에 넣는다.
                                Q.append(arr[k][cc])
                                arr[k][cc] = 0
                        if len(Q): #0인데 그 위에 0아닌 것이 하나라도 있으면
                            jj = 0
                            while Q:# 0이었던 자리부터 차례대로 다시 쌓아준다.
                                arr[rr-jj][cc] = Q.popleft()
                                jj += 1
                        else: #처음 0이 나타났는데 윗줄에 쌓여있는게 없으면 그 열은 다시 보지 않기 위해 no에 열인덱스를 저장해둔다.
                            no.append(cc)
        Min = min(Min, blocks)
        return
    for j in range(W-1,-1,-1):
        makepermu(j, perr)

T = int(input())
for test in range(1, T + 1):
    N, W, H = map(int, input().split())
    Map = []
    Blocks = Min = W * H
    for _ in range(H):
        temp = list(map(int, input().split()))
        Map.append(temp)
        Blocks -= temp.count(0) #처음에 블럭 몇 개 있는지 보기
    Min = W*H
    for i in range(W-1,-1,-1):
        if Min > 0:
            makepermu(i)
    print('#{} {}'.format(test, Min))


# 더 빠르게 혹은 직관적으로 하려면 배열을 1차로 만들어서 .count(0)을 하면 된다.
# 인덱스는 [r*W+c]로 한다.
'''
for c in range(W):
    for r in range(H):
        arr[r*W+c]
'''