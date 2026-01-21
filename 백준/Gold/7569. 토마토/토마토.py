from collections import deque

m, n, h = map(int, input().split())

queue = deque()
visited = [[[False for _ in range(h)] for _ in range(m)] for _ in range(n)]
graph = [[] for _ in range(h)]
for z in range(h):
    for x in range(n):
        graph[z].append(list(map(int, input().split())))
        for y in range(m):
            if graph[z][x][y] == 1:
                queue.append((x, y, z))
                visited[x][y][z] = True
            elif graph[z][x][y] == -1:
                visited[x][y][z] = True

# 동 서 남 북 상 하
dx = [0, 0, 1, -1, 0, 0]
dy = [1, -1, 0, 0, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

def bfs(queue):
    cnt = -1
    while queue:
        tomatos = list(queue)
        queue.clear()
        
        for x, y, z in tomatos:
            for i in range(6):
                nx = x + dx[i]
                ny = y + dy[i]
                nz = z + dz[i]
                
                if nx < 0 or ny < 0 or nz < 0 or nx >= n or ny >= m or nz >= h:
                    continue
                
                if visited[nx][ny][nz] == False and graph[nz][nx][ny] == 0:
                    visited[nx][ny][nz] = True
                    queue.append((nx, ny, nz))
        cnt += 1
        
    if all(all(all(layer) for layer in mat) for mat in visited) == False:
        print(-1)
    else:
        print(cnt)

bfs(queue)