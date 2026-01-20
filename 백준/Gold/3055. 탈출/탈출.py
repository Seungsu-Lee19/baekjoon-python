from collections import deque

r, c = map(int, input().split())
graph = []

start = []
finish = []
for i in range(r):
    a = input()
    graph.append(list(a))
    
    if len(start) == 0:
        y = a.find('S')
        if y >= 0:
            start = [i, y]
    if len(finish) == 0:
        y = a.find('D')
        if y >= 0:
            finish = [i, y]
    
# 상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    queue = deque()
    queue.append(start)
    
    visited = [[0 for _ in range(c)] for _ in range(r)]
    visited[start[0]][start[1]] = 1
    
    while queue:
        items = list(queue)
        queue.clear()
        
        fill = set()
        for i in range(r):
            for j in range(c):
                if graph[i][j] == '*':
                    for k in range(4):
                        nx = i + dx[k]
                        ny = j + dy[k]
                        
                        if nx < 0 or ny < 0 or nx >= r or ny >= c:
                            continue
                        
                        if graph[nx][ny] == '.' or graph[nx][ny] == 'S':
                            fill.add((nx, ny))
        
        for i, j in fill:
            graph[i][j] = '*'

        
        for x, y in items:
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                
                if nx < 0 or ny < 0 or nx >= r or ny >= c:
                    continue
                
                if visited[nx][ny] == 0 and graph[nx][ny] == '.':
                    visited[nx][ny] = visited[x][y] + 1
                    graph[nx][ny] = 'S'
                    graph[x][y] = '.'
                    # graph[nx][ny], graph[x][y] = graph[x][y], graph[nx][ny]
                    queue.append([nx, ny])
                elif visited[nx][ny] == 0 and graph[nx][ny] == 'D':
                    print(visited[x][y])
                    return
            
    print("KAKTUS")

bfs()