n, m = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(input())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

alpha = set(graph[0][0])
_max = 0

def dfs(x, y, cnt):
    global _max
    _max = max(_max, cnt)
    if _max == 26:
        return
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if nx < 0 or ny < 0 or nx >= n or ny >= m:
            continue
        
        if graph[nx][ny] not in alpha:
            alpha.add(graph[nx][ny])
            dfs(nx, ny, cnt + 1)
            alpha.remove(graph[nx][ny])

dfs(0, 0, 1)
print(_max)