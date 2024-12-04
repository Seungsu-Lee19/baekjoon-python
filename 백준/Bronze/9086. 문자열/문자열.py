import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    _str = input().rstrip()
    print(f"{_str[0]}{_str[-1]}")
