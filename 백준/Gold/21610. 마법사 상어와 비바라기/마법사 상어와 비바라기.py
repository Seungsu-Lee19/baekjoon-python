n, m = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
    
cloud = [(n - 1, 0), (n - 1, 1), (n - 2, 0), (n - 2, 1)]

dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]
for _ in range(m):    
    d, s = map(int, input().split())
 
    moveCloud = []
    for i in range(len(cloud)):
        x, y = cloud[i]
        
        nx = (x + dx[d - 1] * s) % n  
        ny = (y + dy[d - 1] * s) % n
        
        graph[nx][ny] += 1
        moveCloud.append((nx, ny))
        
        cnt = 0
        for j in range(1, 5):
            _x = nx + dx[2 * j - 1]
            _y = ny + dy[2 * j - 1]
            
            
            if _x < 0 or _y < 0 or _x >= n or _y >= n:
                continue
            
            if graph[_x][_y] > 0:
                cnt += 1
                continue
            
            bx = (_x + dx[(d + 3) % 8] * s) % n
            by = (_y + dy[(d + 3) % 8] * s) % n
            if (bx, by) in cloud:
                cnt += 1
                
        graph[nx][ny] += cnt
        
    cloud = []
    for i in range(n):
        for j in range(n):
            if graph[i][j] >= 2 and ((i, j) not in moveCloud):
                cloud.append((i, j))
                graph[i][j] -= 2
        
print(sum(sum(row) for row in graph))