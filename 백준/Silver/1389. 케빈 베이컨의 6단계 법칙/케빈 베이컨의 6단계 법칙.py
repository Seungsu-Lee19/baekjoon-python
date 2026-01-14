from collections import deque

def bfs(graph, start, visited):
    queue = deque()
    queue.append(start)
    # visited[start] += 1
    
    while queue:
        # print(queue)
        v = queue.popleft()
        
        for i in graph[v]:
            if visited[i] == 0:
                queue.append(i)
                visited[i] = visited[v] + 1
    _s = 0
    for i in range(1, len(visited)):
        if i != start:
            _s += visited[i]
    
    return _s

n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]

for i in range(m):
    a1, a2 = map(int, input().split())
    graph[a1].append(a2)
    graph[a2].append(a1)

s = []
for i in range(1, n + 1):
    visited = [0] * (n + 1)
    s.append([bfs(graph, i, visited), i])

s.sort()
print(s[0][1])