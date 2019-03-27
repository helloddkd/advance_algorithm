
import sys

sys.stdin = open('ex.txt', 'r')
from math import ceil
N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())
result = 0
for i in range(N):
    result += 0 if A[i] == 0 else 1
    result += ceil((A[i]-B if A[i] > B else 0) /C)
print(int(result))