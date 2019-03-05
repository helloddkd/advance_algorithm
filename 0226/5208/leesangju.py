import sys
sys.stdin = open("5208.txt","r")

def recharge(start, fuel, charge=0):
    global minimum, bus_stop
    if start+fuel >= bus_stop[0]:
        if minimum > charge:
            minimum = charge
        return
    else:
        for i in range(start+1, start+fuel+1):
            if charge + 1 >= minimum: continue
            recharge(i, bus_stop[i],charge+1)

T = int(input())
for test_case in range(1,T+1):
    bus_stop = list(map(int, input().split()))
    minimum = bus_stop[0]
    recharge(1,bus_stop[1])
    print(f"#{test_case} {minimum}")