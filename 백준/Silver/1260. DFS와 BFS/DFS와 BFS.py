from collections import deque

n, m, v = map(int, input().split())

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a1, a2 = map(int, input().split())
    graph[a1].append(a2)
    graph[a2].append(a1)
    
for i in graph:
    i.sort()

def dfs(graph, v, visited):
    visited[v] = True
    
    print(v, end=' ')
    
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

def bfs(graph, start, visited):
    queue = deque()
    queue.append(start)
    
    visited[start] = True
    
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
        

visited = [False] * (n + 1)
dfs(graph, v, visited)
print()

visited = [False] * (n + 1)
bfs(graph, v, visited)