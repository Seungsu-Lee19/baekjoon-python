n = 12
m = 6

graph = []
for _ in range(n):
    graph.append(list(map(str, input())))
    
def dfs(graph, x, y, p, visited):
    if x < 0 or y < 0 or x >= len(graph) or y >= len(graph[0]):
        return False
    if graph[x][y] != p:
        return False
    
    global num
    # 상 하 좌 우
    if visited[x][y] == False:
        # print(x, y, num, graph[x][y], p, visited)
        visited[x][y] = True
        # graph[x][y] = '.'
        num += 1
        
        dfs(graph, x - 1, y, p, visited) # 상
        dfs(graph, x + 1, y, p, visited) # 하
        dfs(graph, x, y - 1, p, visited) # 좌
        dfs(graph, x, y + 1, p, visited) # 우
        
        if num > 3:
            for i in range(len(graph)):
                for j in range(len(graph[0])):
                    if visited[i][j] == True:
                        graph[i][j] = '.'
            
            # print(graph)
            # print(num)
            return True
    
    return False

def apply_gravity(graph, empty='.'):
    n = len(graph)
    m = len(graph[0]) if n else 0

    for c in range(m): # 몇번째 열
        write = n - 1
        for r in range(n - 1, -1, -1): # 몇번째 행  
            if graph[r][c] != empty:
                graph[write][c] = graph[r][c]
                write -= 1
        for r in range(write, -1, -1):
            graph[r][c] = empty
            
cnt = 0
num = 0

while True:
    flag = False
    for i in range(n - 1, -1, -1):
        for j in range(m):
            num = 0
            visited = [[False for _ in range(m)] for _ in range(n)]
            if graph[i][j] == '.':
                continue
            if dfs(graph, i, j, graph[i][j], visited):
                flag = True
            
    if flag:
        cnt += 1
    else:
        print(cnt)
        break
    apply_gravity(graph)
      