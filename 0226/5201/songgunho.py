import sys

sys.stdin = open("5201.txt", "r")
def everybody(arr1, arr2):
    global result
    if arr1 == [] or arr2 ==[]:
        return
    if arr2[-1] >= arr1[-1]:
        result+=arr1[-1]
        everybody(arr1[:-1], arr2[:-1])
    elif arr2[-1] < arr1[-1]:
        everybody(arr1[:-1], arr2[:])
Numb_test = int(input())
for _ in range(Numb_test):
    N, M = list(map(int, input().split()))
    Nwi = sorted(list(map(int, input().split())))
    Mti = sorted(list(map(int, input().split())))
    result = 0
    everybody(Nwi, Mti)
    print(f'#{_+1} {result}')