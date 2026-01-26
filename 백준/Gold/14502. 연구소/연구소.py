from collections import deque
from itertools import combinations

n, m = map(int, input().split())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

zeros = []
virus = []
graph = []
zeors_num = 0
for i in range(n):
    lst = list(map(int, input().split()))
    for j in range(m):
        if lst[j] == 0:
            zeros.append((i, j))
            zeors_num += 1
        elif lst[j] == 2:
            virus.append((i, j))
    graph.append(lst)
    
def bfs(queue, visited):
    cnt = 0
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            
            if graph[nx][ny] == 0 and visited[nx][ny] == 0:
                visited[nx][ny] = visited[x][y] + 1
                cnt += 1
                queue.append((nx, ny))
    return cnt

_max = 0
for pick in combinations(zeros, 3):
    for i, j in pick:
        graph[i][j] = 1
        
    visited = [[0 for _ in range(m)] for _ in range(n)]
    queue = deque()
    for i, j in virus:
        queue.append((i, j))
    cnt = bfs(queue, visited)
    _max = max(_max, zeors_num - cnt - 3)
        
    for i, j in pick:
        graph[i][j] = 0
        
print(_max)