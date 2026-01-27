import copy
n = 4

# 무의미 // 위 // 왼쪽 위 // 왼쪽 // 왼쪽 아래 // 아래 // 오른쪽 아래 // 오른쪽 // 오른쪽 위
dx = [0, -1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 0, -1, -1, -1, 0, 1, 1, 1]

fish = []
fish_idx = [[] for _ in range(17)]
for i in range(n):
    fish.append(list(map(int, input().split())))
    for j in range(n):
        fish_idx[fish[i][j * 2]] = [i, j]

_max = 0
def dfs(x, y, direction, num, eat_list, fish, fish_idx):
    global _max
    
    f = 1
    while f < 17:
        i, j = fish_idx[f]
        
        if eat_list[f]:
            f += 1
            continue
        
        if fish[i][j * 2] == -1:
            f += 1
            continue
        
        
        ni = i + dx[fish[i][j * 2 + 1]]
        nj = j + dy[fish[i][j * 2 + 1]]
        
        if ni < 0 or nj < 0 or ni >= 4 or nj >= 4:
            fish[i][j * 2 + 1] = (fish[i][j * 2 + 1] % 8) + 1
            continue
        if fish[ni][nj * 2] == -1:
            fish[i][j * 2 + 1] = (fish[i][j * 2 + 1] % 8) + 1
            continue
        
        if fish[ni][nj * 2] == 0:
            fish_idx[f] = [ni, nj]
        else:
            fish_idx[f][0], fish_idx[fish[ni][nj * 2]][0] = fish_idx[fish[ni][nj * 2]][0], fish_idx[f][0]
            fish_idx[f][1], fish_idx[fish[ni][nj * 2]][1] = fish_idx[fish[ni][nj * 2]][1], fish_idx[f][1]
        
        fish[ni][nj * 2], fish[i][j * 2] = fish[i][j * 2], fish[ni][nj * 2]
        fish[ni][nj * 2 + 1], fish[i][j * 2 + 1] = fish[i][j * 2 + 1], fish[ni][nj * 2 + 1]
        
        f += 1
    
    cnt = 0
    for i in range(1, 4):
        nx = x + dx[direction] * i
        ny = y + dy[direction] * i
        
        if nx < 0 or ny < 0 or nx >= 4 or ny >= 4:
            _max = max(_max, num)
            return
        if fish[nx][ny * 2] == 0:
            cnt += 1
            if cnt == 3:
                _max = max(_max, num)
                return
            continue
        
        temp = fish[nx][ny * 2]
        eat_list[temp] = True
        fish[x][y * 2] = 0
        fish[nx][ny * 2] = -1
        
        _eat_list = copy.deepcopy(eat_list)
        _fish = copy.deepcopy(fish)
        _fish_idx = copy.deepcopy(fish_idx)
        
        dfs(nx, ny, fish[nx][ny * 2 + 1], num + temp, _eat_list, _fish, _fish_idx)
        
        eat_list[temp] = False
        fish[nx][ny * 2] = temp
        fish[x][y * 2] = -1
    
eat_list = [False] * 17
eat_list[fish[0][0]] = True
num = fish[0][0]
fish[0][0] = -1
dfs(0, 0, fish[0][1], num, eat_list, fish, fish_idx)
print(_max)