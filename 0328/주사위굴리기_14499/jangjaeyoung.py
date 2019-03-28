import sys

sys.stdin = open('14499.txt', 'r')


class Dice:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.head = 0
        self.tail = 5
        self.left = 3
        self.right = 2
        self.front = 4
        self.back = 1
        self.values = [0, 0, 0, 0, 0, 0]
        self.temp = 0

    def roll_right(self):
        self.temp = self.head
        self.head = self.left
        self.left = self.tail
        self.tail = self.right
        self.right = self.temp

        self.y += 1

    def roll_left(self):
        self.temp = self.head
        self.head = self.right
        self.right = self.tail
        self.tail = self.left
        self.left = self.temp

        self.y -= 1

    def roll_up(self):
        self.temp = self.head
        self.head = self.front
        self.front = self.tail
        self.tail = self.back
        self.back = self.temp

        self.x -= 1

    def roll_down(self):
        self.temp = self.head
        self.head = self.back
        self.back = self.tail
        self.tail = self.front
        self.front = self.temp

        self.x += 1

    def color(self, num):
        self.values[self.tail] = num


N, M, x, y, K = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(N)]
command = list(map(int, input().split()))

dice = Dice(x, y)

for c in command:
    if c == 1:
        if 0 <= dice.y + 1 < M:
            dice.roll_right()
            if matrix[dice.x][dice.y] == 0:
                matrix[dice.x][dice.y] = dice.values[dice.tail]
            else:
                dice.color(matrix[dice.x][dice.y])
                matrix[dice.x][dice.y] = 0

            print(dice.values[dice.head])
    elif c == 2:
        if 0 <= dice.y - 1 < M:
            dice.roll_left()
            if matrix[dice.x][dice.y] == 0:
                matrix[dice.x][dice.y] = dice.values[dice.tail]
            else:
                dice.color(matrix[dice.x][dice.y])
                matrix[dice.x][dice.y] = 0

            print(dice.values[dice.head])
    elif c == 3:
        if 0 <= dice.x - 1 < N:
            dice.roll_up()
            if matrix[dice.x][dice.y] == 0:
                matrix[dice.x][dice.y] = dice.values[dice.tail]
            else:
                dice.color(matrix[dice.x][dice.y])
                matrix[dice.x][dice.y] = 0

            print(dice.values[dice.head])
    elif c == 4:
        if 0 <= dice.x + 1 < N:
            dice.roll_down()
            if matrix[dice.x][dice.y] == 0:
                matrix[dice.x][dice.y] = dice.values[dice.tail]
            else:
                dice.color(matrix[dice.x][dice.y])
                matrix[dice.x][dice.y] = 0

            print(dice.values[dice.head])
