from collections import deque

n = 4
m, s = map(int, input().split())

fish = {}
for _ in range(m):
    x, y, d = map(int, input().split())
    fish.setdefault((x - 1, y - 1), []).append(d - 1)
        
x, y = map(int, input().split())
shark = (x - 1, y - 1)

dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]
p = 0
practice = {}
smell = {}

dx2 = [0, 1, 0, -1]
dy2 = [1, 0, -1, 0]
  
while s > 0:
    moveFish = {}
    for (x, y), ds in fish.items():
        for d in ds:
            isMoving = False
            for i in range(8):
                direction = (d - i) % 8
                nx = x + dx[direction]
                ny = y + dy[direction]
                
                if nx < 0 or ny < 0 or nx >= n or ny >= n:
                    continue
                if (nx, ny) != shark and (nx, ny) not in smell:
                    moveFish.setdefault((nx, ny), []).append(direction)
                    isMoving = True
                    break
            if isMoving == False:
                moveFish.setdefault((x, y), []).append(d)
    
    # shark eat fish
    
    _max = -1
    shark_temp = ()
    smell_temp = {}
    for i in range(4):
        nx1 = shark[0] + dx2[i]
        ny1 = shark[1] + dy2[i]
        if nx1 < 0 or ny1 < 0 or nx1 >= n or ny1 >= n:
            continue
        
        for j in range(4):
            nx2 = nx1 + dx2[j]
            ny2 = ny1 + dy2[j]
            if nx2 < 0 or ny2 < 0 or nx2 >= n or ny2 >= n:
                continue
            
            for k in range(4):
                nx3 = nx2 + dx2[k]
                ny3 = ny2 + dy2[k]
                
                if nx3 < 0 or ny3 < 0 or nx3 >= n or ny3 >= n:
                    continue
                nxy = set()
                nxy.add((nx1, ny1))
                nxy.add((nx2, ny2))
                nxy.add((nx3, ny3))
                
                cnt = 0
                _smell = {}
                for x, y in nxy:
                    if (x, y) in moveFish:
                        cnt += len(moveFish[(x, y)])
                        _smell[(x, y)] = 1
                        
                if cnt >= _max:
                    _max = cnt
                    shark_temp = (nx3, ny3)
                    smell_temp = _smell
                    
                
    for k, v in smell_temp.items():
        smell[k] = smell.get(k, 0) + v
        
    practice[p] = smell_temp
    if p >= 2:
        for x, y in practice[p - 2]:
            smell[(x, y)] -= 1
            if smell[(x, y)] == 0:
                del smell[(x, y)]
            
    for x, y in smell_temp:
        del moveFish[(x, y)]
    
    for k, v in moveFish.items():
        fish.setdefault(k, []).extend(v)
        
    shark = shark_temp
    p += 1
    s -= 1
    
total = sum(len(v) for v in fish.values())
print(total)
