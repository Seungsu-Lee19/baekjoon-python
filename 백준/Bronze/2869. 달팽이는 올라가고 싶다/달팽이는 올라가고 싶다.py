import sys
import math
input = sys.stdin.readline

a, b, v = list(map(int, input().split()))

x = math.ceil((v - a) / (a - b))
print(f"{x + 1}")