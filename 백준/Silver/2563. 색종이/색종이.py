import sys
input = sys.stdin.readline

a = [[0 for _ in range(100)] for _ in range(100)]

num = int(input())

for i in range(num):
    start, end = list(map(int, input().split()))

    for x in range(start, start + 10):
        for y in range(end, end + 10):
            a[x][y] = 1

print(sum(sum(row) for row in a))