def bt(data, start, cnt):
    global min_cnt
    if start == data[0]:
        cnt -= 1
        min_cnt = min(min_cnt, cnt)
    else:
        if cnt > min_cnt:
            return min_cnt
        temp = 100
        for i in range(start + 1, data[0] + 1):
            if start + data[start] >= i:
                temp = min(temp, bt(data, i, cnt + 1))
        cnt = temp
    return cnt


for T in range(1, int(input()) + 1):
    inputs = list(map(int, input().split()))
    min_cnt = 100
    result = bt(inputs, 1, 0)
    print(f'#{T} {result}')
