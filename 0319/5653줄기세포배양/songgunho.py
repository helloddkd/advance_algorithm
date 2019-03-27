import sys

sys.stdin = open('5653.txt', 'r')
T = int(input())

class Viper:
    def __init__(self,x,y,size,act,time,dead):
        self.x = x
        self.y = y
        self.size = size
        self.act = act
        self.time = time
        self.dead = dead
    def move(self):
        dix = [0,0,1,-1]
        diy = [1,-1,0,0]
        for i in range(4):
            new_x, new_y = self.x +dix[i], self.y +diy[i]
            new_size, new_act, new_time, new_dead = self.size, False , 0, False
            temp = Viper(new_x, new_y, new_size,new_act, new_time, new_dead)
            if self.act == True and (new_x,new_y) not in que and (new_x,new_y) not in que3:
                if que2.get((new_x, new_y)) is None:
                    que2[(new_x,new_y)] = temp
                else:
                    if que2.get((new_x, new_y)).size > temp.size:
                        continue
                    else:
                        que2[(new_x, new_y)] = temp
    def timepas(self):
        new_x, new_y = self.x, self.y
        new_size, new_act, new_time, new_dead = self.size, True if self.size <= self.time + 1 < self.size * 2 else False, self.time + 1, True if self.time + 1 >= self.size * 2 else False
        if new_dead == True:
            que3[(new_x, new_y)] = Viper(new_x, new_y, new_size,new_act, new_time, new_dead)
        else:
            que2[(new_x, new_y)] = Viper(new_x, new_y, new_size,new_act, new_time, new_dead)


for _ in range(T):
    Y, X, K = map(int, input().split())
    arr = [list(map(int, input().split())) for __ in range(Y)]
    que = {}
    que2 = {}
    que3 = {}
    cnt = 0
    for y in range(Y):
        for x in range(X):
            if arr[y][x] != 0:
                que[(x,y)] = Viper(x,y,arr[y][x],False,0,False)

    for ___ in range(K):
        for key, val in que.items():
            val.move()
            val.timepas()
        else:
            que = que2
            que2 = {}



    for re in que.values():
        if re.dead == False:
            cnt += 1

    print('#{} {}'.format(_+1, cnt))