from collections import deque

n, m, k = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

# 동 남 서 북
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
def bfs(x, y, b):
    queue = deque()
    queue.append((x, y))
    visited = [[0 for _ in range(m)] for _ in range(n)]
    visited[x][y] = 1
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            
            if visited[nx][ny] == 0 and graph[nx][ny] == b:
                visited[nx][ny] = 1
                queue.append((nx, ny))
    
    return sum(sum(row) for row in visited)
    
score = 0
x = 0
y = 1
direction = 0
#     아래, 오, 위, 왼, 앞, 뒤
dice = [3, 1, 4, 6, 5, 2]
for _ in range(k):
    b = graph[x][y]
    score = score + b * bfs(x, y, b)
    
    a = dice[0]
    if a > b:
        direction = (direction + 1) % 4
    elif a < b:
        direction = (direction - 1) % 4
    nx = x + dx[direction]
    ny = y + dy[direction]

    if nx < 0 or ny < 0 or nx >= n or ny >= m:
        direction = (direction + 2) % 4
        nx = x + dx[direction]
        ny = y + dy[direction]
    
    if direction == 0:
        dice[:4] = dice[1:4] + [dice[0]]
    elif direction == 2:
        dice[:4] = [dice[3]] + dice[:3]
    else:   # 아래, 오, 위, 왼, 앞, 뒤
        under = dice[0]
        on = dice[2]
        front = dice[4]
        behind = dice[5]
        
        if direction == 1:
            dice[0] = front
            dice[2] = behind
            dice[4] = on
            dice[5] = under
        else: 
            dice[0] = behind
            dice[2] = front
            dice[4] = under
            dice[5] = on

    x = nx
    y = ny
        
print(score)