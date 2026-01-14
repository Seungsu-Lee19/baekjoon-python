t = int(input())

def dfs(graph, v, visited):
    visited[v] = True
    if visited[graph[v]] != True:
        dfs(graph, graph[v], visited)

for _ in range(t):
    n = int(input())
    a = [0]
    a.extend(list(map(int,input().split())))
    isUsed = [False for _ in range(n + 1)]
    
    cnt = 0
    
    for i in range(1, n + 1):
        if isUsed[i] == False:
            if a[i] == i:
                cnt += 1
                isUsed[i] = True
            else:
                dfs(a, i, isUsed)
                cnt += 1
    print(cnt)
        