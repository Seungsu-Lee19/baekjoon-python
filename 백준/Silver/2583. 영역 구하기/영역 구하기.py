import sys
sys.setrecursionlimit(10**4)
n, m, k = map(int, input().split())

graph = [[0 for _ in range(m)] for _ in range(n)]
for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())

    fill = [1] * (x2 - x1)    
    for y in range(y1, y2):
        graph[y][x1:x2] = fill

s = 0
rect = []

def dfs(x, y):
    global s
    if x < 0 or y < 0 or x >= n or y >= m:
        return False
    
    if graph[x][y] == 0:
        graph[x][y] = 1
        s += 1
        
        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)
        
        return True
    return False

result = 0
for i in range(n):
    for j in range(m):
        isFinish = dfs(i, j)
        if isFinish == True:
            result += 1
            rect.append(s)
            s=0
            
print(result)
rect.sort()
for i in rect:
    print(i, end=' ')
# print(rect)