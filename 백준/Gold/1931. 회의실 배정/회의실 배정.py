N = int(input())

meet = []
for _ in range(N):
    s, f = map(int, input().split())
    meet.append((f, s))

meet.sort()

cnt = 1
prev = meet[0][0]
for i in range(1, len(meet)):
    f, s = meet[i]
    if prev <= s:
        cnt += 1
        prev = f

print(cnt)
    
