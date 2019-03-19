import sys
from collections import deque

sys.stdin = open('4130.txt', 'r')

def vaildity(arr):
    que = deque()
    que2 = deque()
    cnt = 0
    for i in arr:
        if len(que) == 0 or que[0] == i:
            cnt += 1
            que.append(i)
        else:
            new = [que[0],cnt]
            que = deque()
            que.append(i)
            cnt = 1
            if len(que2) == 0:
                que2.append(new)
            else:
                new2 = que2.popleft()
                height = new[0] - new2[0]
                if abs(height) >1:
                    return False
                else:
                    if height == 1:
                        if new2[1] >= X:
                            que2.append(new)
                        else:
                            return False
                    elif height == -1:
                        if new[1] >= X:
                            new[1] -= X
                            que2.append(new)
                        else:
                            return False
    else:
        if len(que2) ==0:
            return True
        new = [que[0], cnt]
        new2 = que2.popleft()
        height = new[0] - new2[0]
        if abs(height) > 1:
            return False
        else:
            if height == 1:
                if new2[1] < X:
                    return False
            elif height == -1:
                if new[1] < X:
                    return False
        return True


T = int(input())
for _ in range(T):
    N, X = map(int, input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]
    cnt = 0
    for i in range(N):
        if vaildity(arr[i][:]):
            cnt += 1
        if vaildity([arr[k][i] for k in range(N)]):
            cnt += 1
    print('#{} {}'.format(_+1,cnt))