from collections import deque

n, k = map(int, input().split())

def bfs(x, k):
    queue = deque()
    queue.append(x)
    
    visited = [0] * (k * 2)
    
    while queue:
        v = queue.popleft()
        
        dx = [v + 1, v - 1, v * 2]
        
        for nx in dx:
            if nx < 0 or nx >= (k * 2):
                continue
            
            if visited[nx] == 0:
                visited[nx] = visited[v] + 1
                queue.append(nx)
            elif visited[nx] > visited[v]:
                visited[nx] = visited[v] + 1
                
    print(visited[k])
    
if n >= k:
    print(n - k)
else:
    bfs(n, k)
         