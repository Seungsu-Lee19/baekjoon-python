import sys
import math
input = sys.stdin.readline

a = int(input())
b = int(input())

c = []
for i in range(a, b+1):
    _int = 1
    temp = 0
    while True:
        if i % _int == 0:
            temp += 1
        _int += 1

        if temp > 2:
            break
        if i < _int:
            break
    
    if temp == 2:
        c.append(i)

if len(c) == 0:
    print("-1")
else:
    print(f"{sum(c)}")
    print(f"{min(c)}")
