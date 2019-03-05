import sys
sys.stdin = open('5185.txt')

T = int(input())
for t in range(T):
    N, num = input().split()
    
    num = '0x' + num
    num = format(int(num, 16), 'b')
    
    if len(num) % 4:
        num = '0' * (4 - len(num) % 4) + num

    print(f'#{t+1} {num}')