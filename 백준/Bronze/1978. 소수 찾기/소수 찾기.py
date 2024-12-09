import sys
import math
input = sys.stdin.readline

a = int(input())
b = list(map(int, input().split()))

cnt = 0
for i in range(a):
    _int = 1
    temp = 0
    while True:
        if b[i] % _int == 0:
            temp += 1

        if temp > 2:
            break
        if b[i] < _int:
            break
        
        _int += 1
    
    if temp == 2:
        cnt += 1
    
print(f"{cnt}")
    

