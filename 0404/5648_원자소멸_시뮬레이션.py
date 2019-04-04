import sys

sys.stdin = open('5648.txt', 'r')

dix = [0,0,-1,1]
diy = [1,-1,0,0]
class Atom_colide:
    global result

    def __init__(self,x ,y, location, size):
        self.x = x
        self.prex = x + dix[location]
        self.y = y
        self.prey = y + diy[location]
        self.location = location
        self.size = size
    # move함수로들어오면 atom temp라는 임시 보관소에 이동한 원자들이 저장된다
    def move(self):
        global result
        x, prex, y, prey, location, size = self.x, self.prex, self.y, self.prey, self.location, self.size
        new_x, new_prex, new_y, new_prey, new_location, new_size = x + dix[location], prex + dix[location],y + diy[location], prey + diy[location], location, size
        if -1000 <= new_x <= 1000 and -1000 <= new_y <= 1000:
            if (prex, prey) in atoms and (atoms[(prex, prey)].prex , atoms[(prex, prey)].prey) == (x,y):
                result += size
                return
            if (new_x, new_y) not in atom_temp and (new_x, new_y) not in temp:
                atom_temp[(new_x, new_y)] = Atom_colide(new_x, new_y, new_location, new_size)
            #중복되는 원자 즉 충돌하는 원자들을 삭제하고 size만큼 result에 더해준다.
            elif (new_x, new_y) in atom_temp:
                result += (new_size + atom_temp[(new_x, new_y)].size)
                temp.append((new_x, new_y))
                del atom_temp[(new_x, new_y)]
                return
            elif (new_x, new_y) in temp:
                result += new_size
                return
T = int(input())
for _ in range(T):
    M = int(input())
    arr = [list(map(int, input().split())) for __ in range(M)]
    atoms = {}
    atom_temp = {}
    temp = []
    result = 0
    for __ in range(len(arr)):
        x, y, location, size = arr[__][0], arr[__][1], arr[__][2], arr[__][3]
        atoms[(x, y)] = Atom_colide(x, y, location, size)
    while True:
        for key, val in atoms.items():
            val.move()
        else:
            if len(atom_temp) == 0:
                break
            else:
                # atom_temp에 저장된 임시 원다르을 다시 atom에 넣어준다.
                atoms = atom_temp
                atom_temp = {}
                temp =[]
    print('#{} {}'.format(_+1 ,result))
