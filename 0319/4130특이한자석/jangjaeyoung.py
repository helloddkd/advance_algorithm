import sys

sys.stdin = open('4130.txt', 'r')


def rotate(magnet, direction):
    if direction == 1:
        temp = magnet.pop(-1)
        magnet.insert(0, temp)
    else:
        temp = magnet.pop(0)
        magnet.append(temp)


T = int(input())
for test_case in range(1, T+1):
    K = int(input())

    magnet1 = list(map(int, input().split()))
    magnet2 = list(map(int, input().split()))
    magnet3 = list(map(int, input().split()))
    magnet4 = list(map(int, input().split()))
    magnet = [magnet1, magnet2, magnet3, magnet4]

    information = []
    for _ in range(K):
        information.append(list(map(int, input().split())))

    for info in information:
        rotates = [0, 0, 0, 0]
        directions = [0, 0, 0, 0]
        if info[0] == 1:
            rotates[0] = 1
            directions[0] = info[1]
            if magnet1[2] != magnet2[6]:
                rotates[1] = 1
                directions[1] = directions[0] * -1
                if magnet2[2] != magnet3[6]:
                    rotates[2] = 1
                    directions[2] = directions[1] * -1
                    if magnet3[2] != magnet4[6]:
                        rotates[3] = 1
                        directions[3] = directions[2] * -1

        elif info[0] == 2:
            rotates[1] = 1
            directions[1] = info[1]
            if magnet2[6] != magnet1[2]:
                rotates[0] = 1
                directions[0] = info[1] * -1

            if magnet2[2] != magnet3[6]:
                rotates[2] = 1
                directions[2] = info[1] * -1
                if magnet3[2] != magnet4[6]:
                    rotates[3] = 1
                    directions[3] = directions[2] * -1

        elif info[0] == 3:
            rotates[2] = 1
            directions[2] = info[1]
            if magnet3[6] != magnet2[2]:
                rotates[1] = 1
                directions[1] = info[1] * -1
                if magnet2[6] != magnet1[2]:
                    rotates[0] = 1
                    directions[0] = directions[1] * -1

            if magnet3[2] != magnet4[6]:
                rotates[3] = 1
                directions[3] = info[1] * -1

        elif info[0] == 4:
            rotates[3] = 1
            directions[3] = info[1]
            if magnet4[6] != magnet3[2]:
                rotates[2] = 1
                directions[2] = info[1] * -1
                if magnet3[6] != magnet2[2]:
                    rotates[1] = 1
                    directions[1] = directions[2] * -1
                    if magnet2[6] != magnet1[2]:
                        rotates[0] = 1
                        directions[0] = directions[1] * -1

        for i in range(4):
            if rotates[i] != 0:
                rotate(magnet[i], directions[i])

    result = 0
    if magnet1[0] == 1:
        result += 1
    if magnet2[0] == 1:
        result += 2
    if magnet3[0] == 1:
        result += 4
    if magnet4[0] == 1:
        result += 8

    print('#{} {}'.format(test_case, result))
