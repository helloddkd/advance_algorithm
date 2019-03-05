binary_nums = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
for T in range(1, int(input()) + 1):
    N, arr = input().split()
    arr = list(arr)
    for i in range(len(arr)):
        arr[i] = int(arr[i]) if arr[i] not in binary_nums else binary_nums[arr[i]]
    result = ''
    for n in arr:
        temp = ''
        for _ in range(4):
            temp += str(n % 2)
            n //= 2
        result += temp[::-1]
    print(f'#{T} {result}')
