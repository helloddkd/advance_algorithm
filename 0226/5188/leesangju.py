import sys
sys.stdin = open("5188.txt","r")

def route(right, down, total_move, total_sum):
    global minimum
    if right + down == total_move:
        if minimum > total_sum:
            minimum = total_sum
        return
    for i in range(2):
        if i == 0 and right < total_move//2:
            if total_sum + arr[right+1][down] >= minimum:continue
            route(right+1, down, total_move, total_sum + arr[right+1][down])
        elif i == 1 and down < total_move//2:
            if total_sum + arr[right][down+1] >= minimum:continue
            route(right, down+1, total_move, total_sum + arr[right][down+1])

T = int(input())
for test_case in range(1,T+1):
    N = int(input())
    arr = [0 for _ in range(N)]
    for n in range(N):
        arr[n] = list(map(int, input().split()))
    minimum = 10*(2*N-2)
    route(0,0,2*N-2, arr[0][0])
    print(f"#{test_case} {minimum}")

