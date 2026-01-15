import copy
import sys

sys.setrecursionlimit(10 ** 4 + 4)

n = int(input())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
    
def dfs(graph, x, y, rain, visited, n):
    if x < 0 or y < 0 or x >= n or y >= n:
        return False
    
    if visited[x][y] == False and graph[x][y] > rain:
        visited[x][y] = True
        
        dfs(graph, x - 1, y, rain, visited, n)
        dfs(graph, x + 1, y, rain, visited, n)
        dfs(graph, x, y - 1, rain, visited, n)
        dfs(graph, x, y + 1, rain, visited, n)
    
        return True
    return False
    

result = [1]
rain = set()
for row in graph:
    rain.update(row)
rain = list(rain)
# rain = list(x for row in graph for x in row)

for k in rain:
    cnt = 0
    _graph = copy.deepcopy(graph)
    visited = [[False for _ in range(n)] for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            if dfs(_graph, i, j, k, visited, n):
                cnt += 1
    result.append(cnt)
print(max(result))

