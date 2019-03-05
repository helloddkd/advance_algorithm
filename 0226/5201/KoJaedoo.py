for T in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    ws = sorted(list(map(int, input().split())), reverse=True)
    ts = sorted(list(map(int, input().split())))
    result = 0
    for t in ts:
        for w in ws:
            if t >= w:
                result += w
                ws.remove(w)
                break
    print(f'#{T} {result}')
