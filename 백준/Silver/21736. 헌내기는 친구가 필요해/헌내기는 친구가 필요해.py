from collections import deque

N, M = map(int, input().split())
x = 0
y = 0

graph = []
for i in range(N):
    graph.append(input())
    
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    q = deque()
    q.append((x, y))
    
    visited = [[False for _ in range(M)] for _ in range(N)]
    visited[x][y] = True
    
    cnt = 0
    while q:
        x, y = q.popleft()
        
        if graph[x][y] == 'P':
            cnt += 1
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                continue
            
            if visited[nx][ny] == False and graph[nx][ny] != 'X':
                visited[nx][ny] = True
                q.append((nx, ny))
    
    if cnt == 0:
        return 'TT'
    return cnt

def findDo():
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 'I':
                return bfs(i, j)

print(findDo())