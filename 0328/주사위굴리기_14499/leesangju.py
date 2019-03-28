import sys
sys.stdin = open("acm_14499.txt", "r")

# 주사위 클래스를 만들었습니다.
class Dice:

    # 각 면을 지정해주었습니다.
    def __init__(self):
        self.side_1 = self.side_2 = self.side_3 = self.side_4 = self.side_5 = self.side_6 = 0

    # 동서남북 방향으로 움직일 때, 각 면이 어떻게 이동하는지를 함수로 나타내었습니다.
    def move_south(self):
        self.side_1, self.side_2, self.side_5, self.side_6 = self.side_2, self.side_6, self.side_1, self.side_5

    def move_north(self):
        self.side_1, self.side_2, self.side_5, self.side_6 = self.side_5, self.side_1, self.side_6, self.side_2

    def move_east(self):
        self.side_1, self.side_3, self.side_4, self.side_6 = self.side_4, self.side_1, self.side_6, self.side_3

    def move_west(self):
        self.side_1, self.side_3, self.side_4, self.side_6 = self.side_3, self.side_6, self.side_1, self.side_4

    # 도착한 지도의 위치에 있는 숫자에 따라 주사위에 생기는 변화와 윗면의 값를 출력하는 함수를 만들었습니다.
    def change_print(self, X, Y):
        global MAP
        if MAP[X][Y] > 0:
            self.side_6, MAP[X][Y] = MAP[X][Y], 0
        elif MAP[X][Y] == 0:
            MAP[X][Y] = self.side_6
        print(self.side_1)


N, M, X, Y, K = map(int, input().split())

# 지도를 저장하였습니다.
MAP = []
for n in range(N):
    MAP += [list(map(int, input().split()))]

# 클래스의 인스턴스를 만들었습니다.
dice = Dice()

order = list(map(int, input().split()))

# 반복문을 사용하여 명령값을 받으며 각각의 값에 따라 동작하도록 하였습니다.
for k in range(K):
    if order[k] == 1:
        if Y + 1 < M:
            Y = Y + 1
            dice.move_east()
            dice.change_print(X, Y)

    elif order[k] == 2:
        if Y - 1 >= 0:
            Y = Y - 1
            dice.move_west()
            dice.change_print(X, Y)

    elif order[k] == 3:
        if X - 1 >= 0:
            X = X - 1
            dice.move_north()
            dice.change_print(X, Y)
    else:
        if X + 1 < N:
            X = X + 1
            dice.move_south()
            dice.change_print(X, Y)

