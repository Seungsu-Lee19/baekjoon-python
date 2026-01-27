r, c, t = map(int, input().split())

graph = []
cleaner = []
for i in range(r):
    lst = list(map(int, input().split()))
    if -1 in lst:
        cleaner.append(i)    
    graph.append(lst)
    
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
for _ in range(t):
    dust = [[0 for _ in range(c)] for _ in range(r)]
    
    for i in range(r):
        for j in range(c):
            if graph[i][j] > 0:
                dust[i][j] += graph[i][j]
                cnt = 0
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    
                    if nx < 0 or ny < 0 or nx >= r or ny >= c:
                        continue
                    if graph[nx][ny] == -1:
                        continue
                    
                    dust[nx][ny] = dust[nx][ny] + int(graph[i][j] / 5)
                    cnt += 1
                dust[i][j] = dust[i][j] - int(graph[i][j] / 5) * cnt
    for i in range(cleaner[0] - 1, 0, -1):
        dust[i][0] = dust[i - 1][0]      
    for i in range(cleaner[1] + 1, r - 1):
        dust[i][0] = dust[i + 1][0] 
        
    for i in range(c - 1):
        dust[0][i] = dust[0][i + 1]
        dust[r - 1][i] = dust[r - 1][i + 1]
        
    for i in range(cleaner[0]):
        dust[i][c - 1] = dust[i + 1][c - 1]
    for i in range(r - 1, cleaner[1], -1):
        dust[i][c - 1] = dust[i - 1][c - 1]
        
    for i in range(c - 1, 0, -1):
        dust[cleaner[0]][i] = dust[cleaner[0]][i - 1]
        dust[cleaner[1]][i] = dust[cleaner[1]][i - 1]
        
    dust[cleaner[0]][0] = -1
    dust[cleaner[1]][0] = -1
    
    graph = dust
print(sum(sum(row) for row in graph) + 2)