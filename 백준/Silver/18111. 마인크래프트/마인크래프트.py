N, M, B = map(int, input().split())

graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))
    
def check(h, block):
    t = 0
    
    for i in range(N):
        for j in range(M):
            gap = (h - graph[i][j])
            if gap > 0:
                t += gap
                block -= gap
            elif gap < 0:
                t += (-gap) * 2
                block += (-gap)
                
    if block >= 0:
        return True, t
    else:
        return False, t
  
time = int(1e9)
height = 0

for i in range(257):
    isCan, t = check(i, B)
    if isCan:
        if t <= time:
            time = t
            height = i
          
print(time, height)
# left = 0
# right = max(max(row for row in graph))
# ans = int(1e9)
# height = 0

# while left <= right:
#     mid = (left + right) // 2
    
#     isCan, t = check(mid, B)
#     if isCan:
#         left = mid + 1
#         if t < ans:
#             ans = t    
#             height = mid
#         elif t == ans:
#             height = max(height, mid)
#     else:
#         right = mid - 1
        
# print(ans, height)