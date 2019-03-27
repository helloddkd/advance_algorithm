import sys
sys.stdin = open('ex.txt','r')

class Dice:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.top = 0
        self.bottom = 0
        self.right = 0
        self.left = 0
        self.head = 0
        self.tail = 0

    def move(self,direction):
        dix = [0,1,-1,0,0]
        diy = [0,0,0,-1,1]
        newx, newy = self.x+ dix[direction], self.y + diy[direction]
        if newx<0 or newx > X-1 or newy <0 or newy > Y-1:
            return True
        else:
            self.x , self.y = newx, newy
            if direction == 1:
                newtop, newbottom, newright, newleft, newhead, newtail = self.left, self.right, self.top, self.bottom, self.head, self.tail
            if direction == 2:
                newtop, newbottom, newright, newleft, newhead, newtail = self.right, self.left, self.bottom, self.top, self.head, self.tail
            if direction == 3:
                newtop, newbottom, newright, newleft, newhead, newtail = self.tail, self.head, self.right, self.left, self.top, self.bottom
            if direction == 4:
                newtop, newbottom, newright, newleft, newhead, newtail = self.head, self.tail, self.right, self.left, self.bottom, self.top
            self.top, self.bottom, self.right, self.left, self.head, self.tail = newtop, newbottom, newright, newleft, newhead, newtail
            if arr[newy][newx] == 0:
                arr[newy][newx] = self.bottom
            elif arr[newy][newx] != 0:
                self.bottom = arr[newy][newx]
                arr[newy][newx] = 0

Y,X,y,x,K = list(map(int, input().split()))
arr = [list(map(int, input().split())) for _ in range(Y)]
orderer = list(map(int, input().split()))

new_dice = Dice(x, y)
for test in orderer:
    valid = new_dice.move(test)
    if valid == True:
        continue
    print(new_dice.top)








