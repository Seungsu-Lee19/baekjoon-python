from collections import deque
import sys

n, m = map(int, input().split())
sys.setrecursionlimit(n * m + 1)

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
    

dx = [-1, 1, 0 ,0]
dy = [0, 0, -1, 1]

def bfs():
    queue = deque()
    queue.append((0, 0))
    
    visited = [[False for _ in range(m)] for _ in range(n)]
    visited[0][0] = True
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            
            if graph[nx][ny] == 0 and visited[nx][ny] == False:
                visited[nx][ny] = True
                queue.append((nx, ny))
                
            if graph[nx][ny] != 0:
                graph[nx][ny] -= 1
    print(graph)

def dfs(x, y, visited):
    visited[x][y] = True
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or ny < 0 or nx >= n or ny >= m:
            continue
        
        if visited[nx][ny] == False and graph[nx][ny] != 0:
            dfs(nx, ny, visited)
    return True

year = 0
while True:
    cnt = 0
    visited = [[False for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if graph[i][j] != 0 and visited[i][j] == False:
                if dfs(i, j, visited):
                    cnt += 1
    
    if cnt >= 2:
        break
    elif cnt == 0:
        year = 0
        break
    
    cnt = 0
    visited = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                cnt += 1
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if nx < 0 or ny < 0 or nx >= n or ny >= m:
                        continue
                    if graph[nx][ny] != 0:
                        visited[nx][ny] += 1
    
    if cnt == n * m:
        break
    
    for i in range(n):
        for j in range(m):
            graph[i][j] = graph[i][j] - visited[i][j] if graph[i][j] >= visited[i][j] else 0
        
    year += 1

print(year)