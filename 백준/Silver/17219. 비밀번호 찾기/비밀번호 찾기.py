N, M = map(int, input().split())

name = {}
pr = []
for i in range(1, N + 1):
    site, password = input().split()
    name[site] = password
for _ in range(M):
    site = input()
    print(name[site])