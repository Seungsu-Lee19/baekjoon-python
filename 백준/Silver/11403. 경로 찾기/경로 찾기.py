from collections import deque

N = int(input())

graph = [[] for _ in range(N)]
for i in range(N):
    l = list(map(int, input().split()))
    for j in range(N):
        if l[j] == 1:
            graph[i].append(j)

def bfs(s, f):
    q = deque()
    q.append(s)
    
    visited = [0 for _ in range(N)]
    # visited[s] = True
    
    while q:
        x = q.popleft()
        
        # if x == f:
        #     return 1
    
        for y in graph[x]:
            if visited[y] == 0:
                visited[y] = 1
                q.append(y)
    
    return visited[f]

for i in range(N):
    for j in range(N):
        print(bfs(i, j), end=' ')
    print()
        