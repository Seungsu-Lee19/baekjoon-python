from collections import deque

k = int(input())

w, h = map(int, input().split())
graph = []

for _ in range(h):
    graph.append(list(map(int, input().split())))
    
# 상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

dx2 = [1, -1, -2, -2, -1, 1, 2, 2]
dy2 = [-2, -2, -1, 1, 2, 2, -1, 1]


def bfs():
    queue = deque()
    queue.append((0, 0, 0))
    
    visited = [[[0 for _ in range(k + 1)] for _ in range(w)] for _ in range(h)]
    
    while queue:
        x, y, c = queue.popleft()
        
        if x == h - 1 and y == w - 1:
            return visited[x][y][c]
        
        for i in range(8):
            if i < 4:
                nx = x + dx[i]
                ny = y + dy[i]
                
                if nx < 0 or ny < 0 or nx >= h or ny >= w:
                    continue
                
                if graph[nx][ny] == 0 and visited[nx][ny][c] == 0:
                    visited[nx][ny][c] = visited[x][y][c] + 1
                    queue.append((nx, ny, c))
        
        if c < k:
            for i in range(8):
                nx = x + dx2[i]
                ny = y + dy2[i]
                
                if nx < 0 or ny < 0 or nx >= h or ny >= w:
                    continue
                
                if graph[nx][ny] == 0 and visited[nx][ny][c] == 0 and visited[nx][ny][c+1] == 0:
                    visited[nx][ny][c + 1] = visited[x][y][c] + 1
                    queue.append((nx, ny, c + 1))
            
    return -1

print(bfs())
                