import sys
input = sys.stdin.readline

n, m = list(map(int, input().split()))

arr = [[0 for _ in range(m)] for _ in range(n)]

for i in range(n*2):
    l = list(map(int, input().split()))
    for j in range(len(l)):
        arr[i % n][j] += l[j]
    
for i in range(n):
    for j in range(m):
        print(f"{arr[i][j]} ", end="")
    print()