from collections import deque

t = int(input())

def bfs(start, end, conv):
    queue = deque()
    queue.append(start)
    
    visited = [False] * len(conv)
    while queue:
        x, y = queue.popleft()
        
        if abs(x - end[0]) + abs(y - end[1]) <= 1000:
            return "happy"
        
        for i in range(len(conv)):
            if visited[i] == False:
                if abs(x - conv[i][0]) + abs(y - conv[i][1]) <= 1000:
                    queue.append((conv[i][0], conv[i][1]))
                    visited[i] = True
    return "sad"

for _ in range(t):
    conv_num = int(input())
    conv = []
    
    house_x, house_y = map(int, input().split())
    for _ in range(conv_num):
        conv.append(list(map(int, input().split())))
    fest_x, fest_y = map(int, input().split())
    
    print(bfs((house_x, house_y), (fest_x, fest_y), conv))
    
    