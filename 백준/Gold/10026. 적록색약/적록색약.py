from collections import deque

N = int(input())

graph1 = []
graph2 = []
for _ in range(N):
    l = input()
    graph1.append(l)
    
    new_l = ''
    for i in range(N):
        if l[i] == 'B':
            new_l += 'B'
        else:
            new_l += 'R'
    graph2.append(new_l)
    
visited1 = [[False for _ in range(N)] for _ in range(N)]
visited2 = [[False for _ in range(N)] for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def bfs(x, y, c, graph, visited):
    visited[x][y] = True
    q = deque()
    q.append((x, y))
    
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or ny < 0 or nx >= N or ny >= N:
                continue
            
            if visited[nx][ny] == False and graph[nx][ny] == c:
                visited[nx][ny] = True
                q.append((nx, ny))

cnt1 = 0
cnt2 = 0 
for i in range(N):
    for j in range(N):
        if visited1[i][j] == False:
            bfs(i, j, graph1[i][j], graph1, visited1)
            cnt1 += 1
        
        if visited2[i][j] == False:
            bfs(i, j, graph2[i][j], graph2, visited2)
            cnt2 += 1

print(cnt1, cnt2)