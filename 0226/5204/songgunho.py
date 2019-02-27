import sys

sys.stdin = open("5204.txt", "r")

def quick_sort(ARRAY):
    ARRAY_LENGTH = len(ARRAY)
    if( ARRAY_LENGTH <= 1):
        return ARRAY
    else:
        PIVOT = ARRAY[0]
        GREATER = [ element for element in ARRAY[1:] if element > PIVOT ]
        LESSER = [ element for element in ARRAY[1:] if element <= PIVOT ]
        return quick_sort(LESSER) + [PIVOT] + quick_sort(GREATER)

Numb_test = int(input())
for _ in range(Numb_test):
    T = int(input())
    arr = list(map(int, input().split()))
    b = quick_sort(arr)
    result = b[len(arr)//2]
    print(f'#{_+1} {result}')