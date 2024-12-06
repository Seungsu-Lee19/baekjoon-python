import sys
import math
input = sys.stdin.readline

a, b = list(map(int, input().split()))

idx = 0
_int = 1
while True:
    if a % _int == 0:
        idx += 1
    
    if idx == b:
        print(f"{_int}")
        break

    if a <= _int:
        print("0")
        break

    _int += 1

