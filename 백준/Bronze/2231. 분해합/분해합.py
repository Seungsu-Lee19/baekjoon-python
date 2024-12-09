import sys
import copy
input = sys.stdin.readline

n = int(input())


for i in range(1, n + 1):
    a = copy.deepcopy(i)
    _sum = a
    while True:
        _sum = _sum + (a % 10)
        a = a // 10

        if a < 1:
            break

    if _sum == n:
        print(i)
        exit()

print("0")