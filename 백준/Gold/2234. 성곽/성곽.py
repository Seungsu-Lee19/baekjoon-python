n, m = map(int, input().split())

graph = []
for _ in range(m):
    graph.append(list(map(int, input().split())))
    
def dfs(graph, x, y, visited, n, m):
    global result
    
    if x < 0 or y < 0 or x >= m or y >= n:
        return False
    if visited[x][y] == True:
        return False
    
    visited[x][y] = True
    ## 상, 하, 좌, 우로 갈 수 있고, 방문하지 않았으면 dfs
    
    for i in range(4):
        b = graph[x][y] & (1 << i)
        if b == 0:
            if i == 0: # 서
                dfs(graph, x, y - 1, visited, n, m)
            elif i == 1: # 북
                dfs(graph, x - 1, y, visited, n, m)
            elif i == 2: # 동
                dfs(graph, x, y + 1, visited, n, m)
            else: # 남
                dfs(graph, x + 1, y, visited, n, m)

    result += 1
    return True
    
    
cnt = 0
_max = []
result = 0
visited = [[False for _ in range(n)] for _ in range(m)]
for i in range(m):
    for j in range(n):
        if dfs(graph, i, j, visited, n, m):
            cnt +=1
            _max.append(result)
            result = 0
            
print(cnt)
print(max(_max))

cnt = 0
_max = []
result = 0
visited = [[False for _ in range(n)] for _ in range(m)]

# 뚫고, 다시 크기 측정

for i in range(m):
    for j in range(n):
        visited = [[False for _ in range(n)] for _ in range(m)]
        for k in range(4):
            b = graph[i][j] & ~(1 << k)
            if b == graph[i][j]:
                continue
            graph[i][j] = b
            
            if dfs(graph, i, j, visited, n, m):
                cnt +=1
                _max.append(result)
                result = 0
                
            graph[i][j] = graph[i][j] | (1 << k)
print(max(_max))
            
