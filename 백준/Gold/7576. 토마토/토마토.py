from collections import deque

N, M = map(int, input().split())

tomato = []
good = deque()
total = 0
day = [[-1 for _ in range(N)] for _ in range(M)]
for i in range(M):
    tom = list(map(int, input().split()))
    for j in range(N):
        if tom[j] == 0:
            total += 1
        elif tom[j] == 1:
            total += 1
            good.append((i, j))   
            day[i][j] = 0
        else:
            day[i][j] = 0
    tomato.append(tom)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    while good:
        x, y = good.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or ny < 0 or nx >= M or ny >= N:
                continue
            
            if tomato[nx][ny] == 0 and day[nx][ny] == -1:
                day[nx][ny] = day[x][y] + 1
                good.append((nx, ny))
                # tomato[nx][ny] = 1

def check():
    _max = -1
    for i in range(M):
        for j in range(N):
            if day[i][j] == -1:
                return -1
            _max = max(_max, day[i][j])
    return _max

bfs()
print(check())
