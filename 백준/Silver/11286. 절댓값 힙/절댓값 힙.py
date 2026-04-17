import heapq

N = int(input())

h = []
ans = []
for _ in range(N):
    x = int(input())
    
    if x != 0:
        heapq.heappush(h, (abs(x), x))
    else:
        a = 0
        if len(h) > 0:
            _, a = heapq.heappop(h)
        
        ans.append(a)

for a in ans:
    print(a)