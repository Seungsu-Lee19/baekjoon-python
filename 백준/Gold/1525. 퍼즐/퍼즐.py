from collections import deque

find = ''
for _ in range(3):
    find += input().replace(" ", "")

start = find.index('0')
# 상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    queue = deque()
    queue.append(find)
    cnt = dict()
    cnt[find] = 0
    
    while queue:
        puzzle = queue.popleft()
        if puzzle == "123456780":
            print(cnt[puzzle])
            return
        
        idx = puzzle.index('0')
        
        x = int(idx // 3)
        y = int(idx % 3)
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or ny < 0 or nx >= 3 or ny >= 3:
                continue
            
            _idx = int(nx * 3 + ny)
            nextNum = list(puzzle)
            nextNum[idx], nextNum[_idx] = nextNum[_idx], nextNum[idx]
            nextNum = "".join(nextNum)
            
            if not cnt.get(nextNum):
                queue.append(nextNum)
                cnt[nextNum] = cnt[puzzle] + 1
    
    print(-1)

bfs()