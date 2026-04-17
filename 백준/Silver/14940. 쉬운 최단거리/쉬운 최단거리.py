from collections import deque

N, M = map(int, input().split())

graph = []
fx = None
fy = None
for i in range(N):
    l = list(map(int, input().split()))
    graph.append(l)
    for j in range(M):
        if l[j] == 2:
            fx = i
            fy = j

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def bfs(sx, sy, visited):
    q = deque()
    q.append((sx, sy))
    
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                continue
            
            if visited[nx][ny] == -1 and graph[nx][ny] == 1:
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx, ny))
            


visited = [[-1 for _ in range(M)] for _ in range(N)]
visited[fx][fy] = 0
bfs(fx, fy, visited)

for i in range(N):
    for j in range(M):
        if graph[i][j] == 0:
            print('0', end=' ')
        else:
            print(visited[i][j], end=' ')
    print()
        