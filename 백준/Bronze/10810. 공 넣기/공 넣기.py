import sys
input = sys.stdin.readline

n, m = list(map(int, input().split()))
backet = [0 for i in range(n)]

for _ in range(m):
    a = list(map(int, input().split()))
    for i in range(a[0]-1, a[1]):
         backet[i] = a[2]
        
for i in range(n):
     print(f'{backet[i]} ', end="")
