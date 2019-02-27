import sys

sys.stdin = open('5208.txt', 'r')

def pathfinder(fuel, way, location=0, recharge=0):
    global result
    if fuel >= way:
        if result > recharge:
            result = recharge
    else:
        for k in range(fuel,0,-1):
            if result > recharge+1:
                pathfinder(array[location+k], way-k, location+k, recharge+1)

Number_test = int(input())
for _ in range(Number_test):
    arr = list(map(int, input().split()))
    M = arr[0]
    array = arr[1:]
    fuel = array[0]
    waytogo = M-1
    result = 101

    pathfinder(fuel, waytogo)
    print(f'#{_+1} {result}')