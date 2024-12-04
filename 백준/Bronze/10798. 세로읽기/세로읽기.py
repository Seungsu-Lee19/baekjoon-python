import sys
input = sys.stdin.readline

a = []
for i in range(5):
    a.append(input().rstrip())

for y in range(15):
    for x in range(5):
        if y < len(a[x]):
            print(a[x][y], end="")