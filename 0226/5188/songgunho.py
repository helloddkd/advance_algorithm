import sys

sys.stdin = open("5188.txt", "r")
def arr_min(x,y,end,result=0):
    result += arr[y][x]
    if x+y == end:
        if result_temp == []:
            result_temp.append(result)
        if result < result_temp[-1]:
            result_temp[0] = result 
    if x<end//2:
        arr_min(x+1,y,end,result)
    if y<end//2:
        arr_min(x,y+1,end,result)

Numb_test = int(input())
for _ in range(Numb_test):
    T = int(input())
    arr = [list(map(int, input().split())) for _ in range(T)]
    result_temp = []
    arr_min(0,0,2*(T-1))
    print(f'#{_+1} {result_temp[0]}')
