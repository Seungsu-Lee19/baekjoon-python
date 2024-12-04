import sys
input = sys.stdin.readline

n, m = list(map(int, input().split()))
backet = [i for i in range(1, n + 1)]

for _ in range(m):
    i, j = list(map(int, input().split()))
    backet[i-1:j] = backet[i-1:j][::-1]
         
for i in range(n):
     print(f'{backet[i]} ', end="")
