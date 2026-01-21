from collections import deque

f, s, g, u, d = map(int, input().split())

# 총 F층
# 스타트링크 G층
# 현재 S층
# U 층으로 가는 버튼
# D 층으로 가는 버튼

visited = [0] * (f + 1)

def bfs():
    queue = deque()
    queue.append(s)
    
    while queue:
        x = queue.popleft()
        
        if x == g:
            return visited[g]
        
        up = x + u
        down = x - d
        
        if up <= f and visited[up] == 0 and u != 0:
            visited[up] = visited[x] + 1
            queue.append(up)
        if down > 0 and visited[down] == 0 and d != 0:
            visited[down] = visited[x] + 1
            queue.append(down)
    return "use the stairs"

print(bfs())
    