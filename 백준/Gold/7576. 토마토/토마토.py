from collections import deque

m, n = map(int, input().split()) # m은 열, n은 행

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

def bfs(graph, queue):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    cnt = -1
    
    while queue:
        x = []
        y = []
        while queue:
            _x, _y = queue.popleft()
            x.append(_x)
            y.append(_y)
        
        for _x, _y in zip(x, y):
            for i in range(4):
                nx = _x + dx[i]
                ny = _y + dy[i]
                
                if nx < 0 or ny < 0 or nx >= n or ny >= m:
                    continue
                if graph[nx][ny] == -1:
                    continue
                
                if graph[nx][ny] == 0:
                    graph[nx][ny] = 1
                    queue.append((nx, ny))
            
        cnt += 1
        
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                print(-1)
                return
            
    print(cnt)

queue = deque()
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            queue.append((i, j))

bfs(graph, queue)
        
    