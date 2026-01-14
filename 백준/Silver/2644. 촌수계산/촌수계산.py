from collections import deque
        
def bfs(_graph, start, finish):
    queue = deque()
    queue.append(start)
    
    visited = [0] * len(_graph)    
    
    while queue:
        v = queue.popleft()
        
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = visited[v] + 1
    
    if visited[finish] > 0:
        print(visited[finish])
    else:
        print(-1)
        
n = int(input())
find = list(map(int, input().split()))
m = int(input())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a1, a2 = map(int, input().split())
    
    graph[a1].append(a2)
    graph[a2].append(a1)


bfs(graph, find[0], find[1])