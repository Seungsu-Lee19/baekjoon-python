N, M = map(int, input().split())

name = {}
pr = []
for i in range(1, N + 1):
    n = input()
    name[n] = 1
for _ in range(M):
    n = input()
    if n in name:
        pr.append(n)

pr.sort()

print(len(pr))
for p in pr:
    print(p)