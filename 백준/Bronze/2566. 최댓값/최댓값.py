import sys
input = sys.stdin.readline

index = [0, 0]
_max = -1
for i in range(9):
    a = list(map(int, input().split()))
    if _max < max(a):
        _max = max(a)
        index[0] = i + 1
        index[1] = a.index(_max) + 1

print(_max)
print(f"{index[0]} {index[1]}")
    