A = int(input())
B = int(input())
C = int(input())

total = str(A * B * C)
cnt = [0 for _ in range(10)]

for s in total:
    cnt[int(s)] += 1

for c in cnt:
    print(c)


