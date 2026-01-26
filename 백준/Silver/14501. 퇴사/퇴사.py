n = int(input())
sche = []
for _ in range(n):
    sche.append(list(map(int, input().split())))
    
d = [0] * (n + 1)
for i in range(0, n):
    for j in range(i + sche[i][0], n + 1):
        if d[j] < d[i] + sche[i][1]:
            d[j] = d[i] + sche[i][1]
print(d[n])