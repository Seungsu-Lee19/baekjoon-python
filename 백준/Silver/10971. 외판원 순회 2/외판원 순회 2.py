n = int(input())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
    
_min = 1000000 * n
_start = 0
def dfs(start, visited, cost, cnt):
    global _min
    global _start
    if cost >= _min:
        return
    if cnt == n - 1:
        if _min > cost + graph[start][_start] and graph[start][_start] != 0:
            _min = cost + graph[start][_start]

    for i in range(n):
        if graph[start][i] != 0 and visited[i] == False:
            visited[i] = True    
            dfs(i, visited, cost + graph[start][i], cnt + 1)        
            visited[i] = False
    
for i in range(n):
    _visited = [False] * n
    _visited[i] = True
    _start = i
    dfs(i, _visited, 0, 0)
print(_min)
    