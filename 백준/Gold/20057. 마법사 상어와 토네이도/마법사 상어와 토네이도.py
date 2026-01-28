n = int(input())

center = int(n / 2)
x = center
y = x
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
    
# 왼, 아, 오, 위
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

ratio = [[[0, 0, 0.02, 0, 0], [0, 0.1, 0.07, 0.01, 0], [0.05, 0, 0, 0, 0], [0, 0.1, 0.07, 0.01, 0], [0, 0, 0.02, 0, 0]]]
ratio.append([list(row) for row in zip(*ratio[0])][::-1])
ratio.append([list(row) for row in zip(*ratio[1])][::-1])
ratio.append([list(row) for row in zip(*ratio[2])][::-1])

direction = 0
isRoation = 1
rotation_num = 1
rot_k = 1

sand = 0
while True:
    if x == 0 and y == 0:
        break
    
    nx = x + dx[direction]
    ny = y + dy[direction]
    
    curSand = graph[nx][ny]
    
    if curSand != 0:
        moveSand = 0
        for i in range(5):
            for j in range(5):
                if ratio[direction][i][j] == 0: continue
                
                _x = 0
                _y = 0
                if i < 2 and j < 2:     # 왼쪽 위
                    _x = nx - 1
                    _y = ny - 1
                elif i < 2 and j > 2:   # 오른쪽 위
                    _x = nx - 1
                    _y = ny + 1
                elif i > 2 and j < 2:   # 왼쪽 아래
                    _x = nx + 1
                    _y = ny - 1
                elif i > 2 and j > 2:   # 오른쪽 아래
                    _x = nx + 1
                    _y = ny + 1
                elif i == 2 and j < 2:  # 왼쪽
                    _x = nx
                    _y = ny + (j - 2)
                elif i == 2 and j > 2:  # 오른쪽
                    _x = nx
                    _y = ny + j - 2
                elif i < 2 and j == 2:  # 위
                    _x = nx + (i - 2)
                    _y = ny
                elif i > 2 and j == 2:  # 아래
                    _x = nx + i - 2
                    _y = ny
                    
                s = int(curSand * ratio[direction][i][j])
                if _x < 0 or _y < 0 or _x >= n or _y >= n:
                    sand += s
                else:
                    graph[_x][_y] += s
                moveSand += s
        
        _x = nx + dx[direction]
        _y = ny + dy[direction]
        alpha = curSand - moveSand   
        if _x < 0 or _y < 0 or _x >= n or _y >= n:
            sand += alpha
        else:
            graph[_x][_y] += alpha
        graph[nx][ny] = 0
                    
    if isRoation == rotation_num:
        isRoation = 0
        direction = (direction + 1) % 4
        if rot_k == 2:
            rot_k = 1
            rotation_num += 1
        else:
            rot_k += 1
    isRoation += 1
    
    x = nx
    y = ny

print(sand)
    
    