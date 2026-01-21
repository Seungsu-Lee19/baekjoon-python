n, m = map(int, input().split())
r, c, d = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

clean = [[0 for _ in range(m)] for _ in range(n)]

# 북 동 남 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

cnt = 0
while True:
    if clean[r][c] == 0:
        clean[r][c] = 1
        cnt += 1
    
    isClean = True
    for i in range(4):
        nx = r + dx[i]
        ny = c + dy[i]

        if nx < 0 or ny < 0 or nx >= n or ny >= m:
            continue
        
        # if clean[nx][ny] == 0:
        #     isClean = False
        
        if clean[nx][ny] == 0 and graph[nx][ny] == 0:
            isClean = False
            
    if isClean == True:
        nx = r + dx[(d - 2) % 4]
        ny = c + dy[(d - 2) % 4]
        
        if nx < 0 or ny < 0 or nx >= n or ny >= m:
            break
        if graph[nx][ny] == 1:
            break
        
        r = nx
        c = ny
    else:
        d = (d - 1) % 4
        
        nx = r + dx[d]
        ny = c + dy[d]
        
        if nx < 0 or ny < 0 or nx >= n or ny >= m:
            continue
        if graph[nx][ny] == 1:
            continue
        if clean[nx][ny] == 0:
            r = nx
            c = ny
print(cnt)
