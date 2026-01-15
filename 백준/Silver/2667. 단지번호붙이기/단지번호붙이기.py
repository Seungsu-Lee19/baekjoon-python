n = int(input())

graph = []
for _ in range(n):
    graph.append(list(map(int, input())))


def dfs(graph, x, y, n):
    global cnt
    
    if x < 0 or y < 0 or x >= n or y >= n:
        return False
    
    if graph[x][y] == 1:
        graph[x][y] = 0
        cnt += 1
        
        dfs(graph, x - 1, y, n)
        dfs(graph, x + 1, y, n)
        dfs(graph, x, y - 1, n)
        dfs(graph, x, y + 1, n)
        
        return True
    
    return False

result1 = 0
result2 = []
cnt = 0

for i in range(n):
    for j in range(n):
        if dfs(graph, i, j, n):
            result1 += 1
            result2.append(cnt)
            cnt = 0

result2.sort()
print(result1)
for i in result2:
    print(i)
    
# print(result)