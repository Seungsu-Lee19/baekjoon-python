import sys
import math
input = sys.stdin.readline

x, y, w, h = list(map(int, input().split()))

a = [x, y, w - x, h - y]
print(f"{min(a)}")