import sys
import math
input = sys.stdin.readline

x = []
y = []

for _ in range(3):
    a, b = list(map(int, input().split()))
    x.append(a)
    y.append(b)

if x[0] != x[1] and x[0] != x[2] and x[1] == x[2]:
    print(f"{x[0]} ", end="")
elif x[1] != x[0] and x[1] != x[2] and x[0] == x[2]:
    print(f"{x[1]} ", end="")
else:
    print(f"{x[2]} ", end="")

if y[0] != y[1] and y[0] != y[2] and y[1] == y[2]:
    print(f"{y[0]}")
elif y[1] != y[0] and y[1] != y[2] and y[0] == y[2]:
    print(f"{y[1]}")
else:
    print(f"{y[2]}")