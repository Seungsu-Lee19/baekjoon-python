n = int(input())
s = int(input())

graph = [[] for _ in range(n + 1)]
for _ in range(s):
    a1, a2 = map(int, input().split())
    graph[a1].append(a2)
    graph[a2].append(a1)
    

def dfs(graph, v, visited):
    visited[v] = True
    
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

visited = [False] * (n + 1)
dfs(graph, 1, visited)
cnt = 0
for i in visited:
    if visited[i] == True:
        cnt += 1

print(cnt - 1)