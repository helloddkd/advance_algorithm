import sys

sys.stdin = open('2382.txt', 'r')


# 같은 속성을 갖는 미생물 객체를 관리할 때 클래스를 사용하면 편할 것 같아서 사용했습니다.
class Micro:
    def __init__(self, x, y, number, direction):
        self.x = x
        self.y = y
        self.number = number  # 현재 미생물 군집 수
        self.original_number = number  # 미생물 군집 수 원본. 미생물 객체들이 합쳐질 때, 미생물 객체의 방향을 정하기 위해 사용했습니다.
        self.direction = direction

    def go(self):
        # 이동하기 전에 지도에서 객체의 흔적을 지웁니다
        if MAP[self.x][self.y] is self:
            MAP[self.x][self.y] = False

        if self.direction == 1:
            # 객체의 방향에 따라 객체를 이동시킵니다.
            self.x += -1

            # 객체가 가장자리에 존재한다면, 방향과 미생물 수를 조정합니다.
            if self.x == 0:
                self.direction = 2
                self.number //= 2
                self.original_number = self.number

            # 객체를 지도에 기록하는 작업입니다.
            # 먼저, 지도를 살펴본 후 비어있다면 그냥 넣습니다.
            if not MAP[self.x][self.y]:
                MAP[self.x][self.y] = self

            # 기록하려는 좌표에 방문표시가 되어 있다면 이미 지도에 기록된 객체와 원본 미생물 수를 비교한 후 합칩니다.
            elif visit[MAP[self.x][self.y].x][MAP[self.x][self.y].y]:
                if MAP[self.x][self.y].original_number > self.original_number:
                    MAP[self.x][self.y].number += self.number
                else:
                    self.number += MAP[self.x][self.y].number
                    MAP[self.x][self.y] = self

            # 이 경우는 좌표 방문 표시가 없는 경우에도 그냥 넣습니다. 지도를 하나만 쓰느라 이런 분기가 필요해졌습니다.
            else:
                MAP[self.x][self.y] = self

        elif self.direction == 2:
            self.x += 1
            if self.x == N-1:
                self.direction = 1
                self.number //= 2
                self.original_number = self.number

            if not MAP[self.x][self.y]:
                MAP[self.x][self.y] = self
            elif visit[MAP[self.x][self.y].x][MAP[self.x][self.y].y]:
                if MAP[self.x][self.y].original_number > self.original_number:
                    MAP[self.x][self.y].number += self.number
                else:
                    self.number += MAP[self.x][self.y].number
                    MAP[self.x][self.y] = self
            else:
                MAP[self.x][self.y] = self

        elif self.direction == 3:
            self.y += -1
            if self.y == 0:
                self.direction = 4
                self.number //= 2
                self.original_number = self.number

            if not MAP[self.x][self.y]:
                MAP[self.x][self.y] = self
            elif visit[MAP[self.x][self.y].x][MAP[self.x][self.y].y]:
                if MAP[self.x][self.y].original_number > self.original_number:
                    MAP[self.x][self.y].number += self.number
                else:
                    self.number += MAP[self.x][self.y].number
                    MAP[self.x][self.y] = self
            else:
                MAP[self.x][self.y] = self

        elif self.direction == 4:
            self.y += 1
            if self.y == N-1:
                self.direction = 3
                self.number //= 2
                self.original_number = self.number

            if not MAP[self.x][self.y]:
                MAP[self.x][self.y] = self
            elif visit[MAP[self.x][self.y].x][MAP[self.x][self.y].y]:
                if MAP[self.x][self.y].original_number > self.original_number:
                    MAP[self.x][self.y].number += self.number
                else:
                    self.number += MAP[self.x][self.y].number
                    MAP[self.x][self.y] = self
            else:
                MAP[self.x][self.y] = self


T = int(input())
for test_case in range(1, T+1):
    N, M, K = map(int, input().split())

    # 자료 구조 1: 현재 유지 관리하고 있는 객체 주소를 담는 리스트
    object_list = [0] * K
    for i in range(K):
        x, y, number, direction = map(int, input().split())
        object_list[i] = Micro(x, y, number, direction)

    # 자료 구조 2: 현재 미생물 객체의 위치를 표시해놓는 지도입니다. 값으로는 객체 주소를 담았습니다.
    MAP = [[False] * N for _ in range(N)]
    # M 시간 동안 반복
    for _ in range(M):
        # 자료 구조 3: 미생물 이동시 그 좌표를 방문 표시하는 리스트. 미생물이 해당 좌표로 이동하기 전에 이미 방문한 미생물 객체가 있는 경우, 합치는 작업이 필요해서 만들었습니다.
        visit = [[False] * N for _ in range(N)]

        # 관리하고 있는 객체 주소를 가지고 미생물들을 이동시킵니다. 다음 번에 쓸 객체 주소를 모으기 위해 temp에 이동한 좌표를 모읍니다.
        temp = []
        for i in range(len(object_list)):
            object_list[i].go()
            if not visit[object_list[i].x][object_list[i].y]:
                visit[object_list[i].x][object_list[i].y] = True
                temp.append([object_list[i].x, object_list[i].y])

        # temp에 모아 놓은 좌표를 가지고 object_list에 객체 주소를 모읍니다.
        object_list = []
        for t in temp:
            object_list.append(MAP[t[0]][t[1]])
            MAP[t[0]][t[1]].original_number = MAP[t[0]][t[1]].number

    # M 시간이 지난 후, 마지막으로 모아 놓은 객체 주소의 모든 미생물 수를 더합니다.
    result = 0
    for o in object_list:
        result += o.number

    print('#{} {}'.format(test_case, result))
