from collections import deque

n, m = list(map(int, input().split()))

graph = []
for _ in range(n):
    graph.append(list(map(int,input().strip())))

# 상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    queue = deque()
    queue.append((0, 0, 0))
    
    visited = [[[0 for _ in range(2)] for _ in range(m)] for _ in range(n)]
    visited[0][0][0] = 1
    
    while queue:
        x, y, c = queue.popleft()
        
        if x == n-1 and y == m - 1:
            print(visited[x][y][c])
            return
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            
            if graph[nx][ny] == 1 and c == 0:
                visited[nx][ny][1] = visited[x][y][0] + 1
                queue.append((nx, ny, 1))
            elif graph[nx][ny] == 0 and visited[nx][ny][c] == 0:
                visited[nx][ny][c] = visited[x][y][c] + 1
                queue.append((nx, ny, c))
                
    print(-1)
    
bfs()