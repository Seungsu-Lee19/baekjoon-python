n = int(input())
dragon = [[0 for _ in range(101)] for _ in range(101)]

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
def cw(x, y, d, g):
    global dragon
    
    lst = [(x, y)]
    nx = x + dx[d]
    ny = y + dy[d]
    lst.append((nx, ny))
    
    dragon[x][y] = 1
    dragon[nx][ny] = 1
    
    candi = [(nx, ny)]
    
    for k in range(g):
        x, y = candi[0]
        dragon[x][y] = 1
        candi = []
        
        for i, j in lst:
            nx = x - (j - y)
            ny = y + (i - x)
            if nx < 0 or ny < 0 or nx >= 101 or ny >= 101:
                continue
            if nx == x and ny == y:
                continue
            candi.append((nx, ny))
            dragon[nx][ny] = 1
        lst = lst + candi
    
for _ in range(n):
    x, y, d, g = map(int, input().split())
    cw(x, y, d, g)

cnt = 0
for i in range(100):
    for j in range(100):
        if dragon[i][j] == 1:
            if dragon[i + 1][j] + dragon[i][j + 1] + dragon[i + 1][j + 1] == 3:
                cnt += 1
                
print(cnt)