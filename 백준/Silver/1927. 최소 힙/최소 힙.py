import heapq

N = int(input())
min_heap = []
l = 0
ans = []

for _ in range(N):
    x = int(input())
    
    if x > 0:
        heapq.heappush(min_heap, x)
        l += 1
    else:
        a = 0
        if l > 0:
            a = heapq.heappop(min_heap)
            l -= 1
        
        ans.append(a)

for a in ans:
    print(a)