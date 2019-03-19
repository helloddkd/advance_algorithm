import sys
from collections import deque

sys.stdin = open('4130.txt', 'r')

T = int(input())

class Magnet:
    def __init__(self, arr, number, nearby):
        self.magnet = deque(arr)
        self.moved = False
        self.number = number
        self.nearby = nearby

    def move(self,ang):
        # print(ang,self.number,self.nearby)
        self.moved = True
        for next in self.nearby:
            if next[1] == 6:
                if self.magnet[6] != mag[next[0]].magnet[2] and mag[next[0]].moved == False:
                    mag[next[0]].move(ang*(-1))
            if next[1] == 2:
                if self.magnet[2] != mag[next[0]].magnet[6] and mag[next[0]].moved == False:
                    mag[next[0]].move(ang*(-1))
        self.magnet.rotate(ang)

for _ in range(T):
    N = int(input())
    arr = [list(map(int, input().split())) for i in range(4)]
    rota = [list(map(int, input().split())) for i in range(N)]
    mag = []
    for y in range(4):
        if y == 0:
            nearby = [[1,2]]
        if 3>y>0:
            nearby = [[y-1,6],[y+1,2]]
        if y==3:
            nearby = [[2,6]]
        mag.append(Magnet(arr[y], y, nearby))

    # for y in mag:
    #     print(y.nearby)
    # print(N)
    # print(rota)
    #
    # for pk in arr:
    #     print(pk)

    for j in range(N):
        mag[rota[j][0]-1].move(rota[j][1])
        for i in mag:
            # print(i.magnet)
            i.moved = False

    result = 0
    for p in range(4):
        result += 2**p if mag[p].magnet[0] == 1 else 0
    print('#{} {}'.format(_+1,result))


