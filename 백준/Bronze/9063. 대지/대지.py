import sys
import math
input = sys.stdin.readline

a = int(input())

if a == 1:
    print("0")
    exit()

x = []
y = []
for _ in range(a):
    i, j = list(map(int, input().split()))
    x.append(i)
    y.append(j)

print(f"{(max(x) - min(x)) * (max(y) - min(y))}")