import heapq

N = int(input())
x = list(map(int, input().split()))
min_heap = []
ans = [0 for _ in range(N)]

for i in range(N):
    heapq.heappush(min_heap, (x[i], i))

prev_x = None
prev_i = None

while min_heap:
    _x, i = heapq.heappop(min_heap)
    
    if prev_x is None:
        prev_x = _x
        prev_i = i
        ans[i] = 0
    else:
        if _x == prev_x:
            ans[i] = ans[prev_i]
        else:
            ans[i] = ans[prev_i] + 1
            prev_x = _x
            prev_i = i

print(*ans) 