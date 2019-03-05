import sys
sys.stdin = open("5185.txt", "r")

T = int(input())
for t in range(1,T+1):
    Nhxd = list(map(str, input().split()))
    N = int(Nhxd[0])
    hxd = Nhxd[1]
    answer = ""
    num_exchange = {"A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15}
    for n in range(N):
        bnum = ""
        if hxd[n] in num_exchange.keys():
            number = num_exchange[hxd[n]]
        else:
            number = int(hxd[n])
        while number > 0 :
            bnum = str(number % 2) + bnum
            number //= 2
        if len(bnum) < 4:
            bnum = "0"*(4-len(bnum)) + bnum
        answer += bnum
    print(f"#{t} {answer}")


