import heapq

N = int(input())
ans = []
max_heap = []

for _ in range(N):
    x = int(input())
    
    if x > 0:
        heapq.heappush(max_heap, -x)
    else:
        a = 0
        if len(max_heap) > 0:
            a = heapq.heappop(max_heap)
            a = -a
            
        ans.append(a)

for a in ans:
    print(a)
