import sys

sys.stdin = open('ex.txt', 'r')



def DFS(arr, n = 0):
    global result,cnt
    cnt += 1
    if n==5:
        result = max(result, max([max(i) for i in arr]))
    else:
        # for i in arr:
        #     print(i)
        #아래방향
        faker = [[0] * N for _ in range(N)]
        for x in range(N):
            now = N-1
            remain = 0
            for y in range(N-1,-1,-1):
                if arr[y][x] == 0:
                    continue
                if arr[y][x]:
                    if remain == 0:
                        remain = arr[y][x]
                    else:
                        if remain == arr[y][x]:
                            faker[now][x] = remain*2
                            remain = 0
                            now -= 1
                        elif remain != arr[y][x]:
                            faker[now][x] = remain
                            now -= 1
                            remain = arr[y][x]
            else:
                faker[now][x] = remain
        # print('down')
        # for i in faker:
        #     print(i)

        DFS(faker,n+1)


        # 위방향
        faker = [[0] * N for _ in range(N)]
        for x in range(N):
            now = 0
            remain = 0
            for y in range(N):
                if arr[y][x] == 0:
                    continue
                if arr[y][x]:
                    if remain ==0:
                        remain = arr[y][x]
                    else:
                        if remain == arr[y][x]:
                            faker[now][x] = remain*2
                            remain = 0
                            now += 1
                        elif remain != arr[y][x]:
                            faker[now][x] = remain
                            now += 1
                            remain = arr[y][x]
            else:
                faker[now][x] = remain
        # print('up')
        # for i in faker:
        #     print(i)
        DFS(faker, n+1)

        # 왼쪽방향
        faker = [[0] * N for _ in range(N)]
        for y in range(N):
            now = 0
            remain = 0
            for x in range(N):
                if arr[y][x] == 0:
                    continue
                if arr[y][x]:
                    if remain ==0:
                        remain = arr[y][x]
                    else:
                        if remain == arr[y][x]:
                            faker[y][now] = remain*2
                            remain = 0
                            now += 1
                        elif remain != arr[y][x]:
                            faker[y][now] = remain
                            now += 1
                            remain = arr[y][x]
            else:
                faker[y][now] = remain
        # print('left')
        # for i in faker:
        #     print(i)
        DFS(faker, n+1)

        #아래방향
        faker = [[0] * N for _ in range(N)]
        for y in range(N):
            now = N-1
            remain = 0
            for x in range(N-1,-1,-1):
                if arr[y][x] == 0:
                    continue
                if arr[y][x]:
                    if remain == 0:
                        remain = arr[y][x]
                    else:
                        if remain == arr[y][x]:
                            faker[y][now] = remain*2
                            remain = 0
                            now -= 1
                        elif remain != arr[y][x]:
                            faker[y][now] = remain
                            now -= 1
                            remain = arr[y][x]
            else:
                faker[y][now] = remain
        # print('right')
        # for i in faker:
        #     print(i)
        DFS(faker,n+1)




N = int(input())
arr2 = [list(map(int, input().split())) for _ in range(N)]
cnt = 0
result = 0
DFS(arr2)
print(result)
# print(cnt)
