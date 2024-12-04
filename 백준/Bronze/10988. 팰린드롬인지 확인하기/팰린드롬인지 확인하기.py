import sys
input = sys.stdin.readline

a = input().rstrip()

for i in range(len(a) // 2):
    if a[i] != a[::-1][i]:
        print("0")
        exit()

print('1')
