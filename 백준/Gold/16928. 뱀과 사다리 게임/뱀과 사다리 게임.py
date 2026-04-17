from collections import deque

N, M = map(int, input().split())

ladder = {}
snake = {}

dp = [int(1e9) for _ in range(101)]
dp[0] = 0

for _ in range(N):
    x, y = map(int, input().split())
    ladder[x] = y
    
for _ in range(M):
    x, y = map(int, input().split())
    snake[x] = y


def bfs():
    q = deque()
    q.append(1)
    
    visited = [-1 for _ in range(101)]
    visited[1] = 0
    
    while q:
        x = q.popleft()
        
        if x in snake:
            continue
        
        for i in range(1, 7):
            nx = x + i
            if nx > 100:
                break
            
            if nx in ladder:
                nx = ladder[nx]
            elif nx in snake:
                nx = snake[nx]
                
            
            if visited[nx] == -1 :
                visited[nx] = visited[x] + 1
                q.append(nx)
                
    
    return visited[100]

print(bfs())