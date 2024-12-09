import sys
input = sys.stdin.readline

a = list(map(int, input().split()))

if 2 * max(a) >= sum(a):
    print(f"{2 * (sum(a) - max(a)) - 1}")
else:
    print(f"{sum(a)}")