from bisect import bisect_left
import sys

input = sys.stdin.readline

N = int(input().strip())

X = list(map(int, input().split()))

coordinate = sorted(list(set(X)))

ans = {}

for i in range(N):
    print(bisect_left(coordinate, X[i]), end=' ')