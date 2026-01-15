n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a1, a2 = map(int, input().split())
    graph[a1].append(a2)
    graph[a2].append(a1)

def bfs(graph, v, visited):
    if visited[v] == True:
        return False
    
    visited[v] = True
    for i in graph[v]:
        if visited[i] == False:
            bfs(graph, i, visited)
        
    return True 
    
cnt = 0
visited = [False] * (n + 1)
for i in range(1, n + 1):
    if bfs(graph, i, visited):
        cnt += 1

print(cnt)