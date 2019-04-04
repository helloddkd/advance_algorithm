import sys
sys.stdin = open('2117.txt', 'r')

T = int(input())
for test in range(1,T+1):
    N,M = map(int, input().split())
    arr = []
    for _ in range(N):
        arr.append(list(map(int, input().split())))

    if N % 2: #홀수개의 변이라면, N만큼의 크기 마름모로 전부 커버 가능
        K = N
    else:#짝수개라면 N+1 크기 마름모로 전부 커버 가능.
        K = N+1
    Max = 0

    for r in range(N):
        for c in range(N):
            for k in range(K, -1, -1):
                S = 0
                for rr in range(r-k+1, r+k):
                    for cc in range(c-k+1, c+k):
                        if 0<=rr<N and 0<=cc<N and abs(rr-r) + abs(cc-c) < k and arr[rr][cc] > 0: #남은 건 마름모 판단하는 법 뿐 ^_^ 중심과의 r차이 c차이 절대값 더해서 마름모 크기보다 작으면 마름모 안에 있는 셀인 것
                            S += 1
                if S*M >= k*k + (k-1)*(k-1):
                    Max = max(Max, S)
    print('#{} {}'.format(test, Max))


#실행시간을 더 줄이고 싶으면 dfs로 해야 함. 모든 칸을 다 보는 게 아니라, home 리스트 안에 잇는 애들만 봐야 함.

#젤 느린거: 내꺼. 모든 지점에서 모든 마름모 다 만든다. 돌아가긴 돌아감.
#중간: BFS로 모든 지점에서 사이즈 키워가면서 안에 집 몇개있는지 센다. 이 때 딱 마름모 내의 r과 c만 작업해서 더 빠르다.
#제일 빠른거: 집이 있는 애들을 따로 저장해놓고, 집 개수만큼만 반복해서 작업한다.