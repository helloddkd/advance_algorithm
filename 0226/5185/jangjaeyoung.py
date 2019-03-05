import sys

sys.stdin = open('5185.txt')

T = int(input())
for test_case in range(1, T+1):
    N, numbers = input().split()

    result = ''
    for number in numbers:
        if number == 'A':
            num = 10
        elif number == 'B':
            num = 11
        elif number == 'C':
            num = 12
        elif number == 'D':
            num = 13
        elif number == 'E':
            num = 14
        elif number == 'F':
            num = 15
        else:
            num = int(number)

        cnt = 0
        while cnt < 4:
            if num // (2**(3-cnt)) == 1:
                result += '1'
                num -= (2**(3-cnt))
            else:
                result += '0'

            cnt += 1

    print(f'#{test_case} {result}')
