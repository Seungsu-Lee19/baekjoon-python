import sys
input = sys.stdin.readline

n, m = list(map(int, input().split()))
a = list(map(int, input().split()))

_max = 0

for i in range(n-2):
    for j in range(i+1, n - 1):
        for k in range(j+1, n):
            if _max < (a[i] + a[j] + a[k]) and (a[i] + a[j] + a[k]) <= m:
                _max = a[i] + a[j] + a[k]
            if _max == m:
                print(f"{_max}")
                exit()

print(f"{_max}")