n, l = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
    
cnt = 0

for i in range(n):
    j = 0
    bridge = [0] * n
    isPosible = True
    while j < n - 1:
        height = graph[i][j] - graph[i][j + 1]
        if height == 0:
            j += 1
            continue
        if abs(height) >= 2:
            isPosible = False
            break
        if bridge[j] != 0 and bridge[j] !=  height:
            isPosible = False
            break
        
        if height == 1: # 내려감
            for k in range(l):
                if j + k + 1 >= n:
                    isPosible = False
                    break
                if graph[i][j] - graph[i][j + 1 + k] != height:
                    isPosible = False
                    break
                bridge[j + k + 1] = 1
            j += l
                
        elif height == -1: # 올라감
            for k in range(l):
                if j - k < 0:
                    isPosible = False
                    break
                if graph[i][j - k] - graph[i][j + 1] != height:
                    isPosible = False
                    break
                if bridge[j - k] != 0:
                    isPosible = False
                    break
                bridge[j - k] = -1
            j += 1
        
        if isPosible == False:
            break
    if isPosible:
        cnt += 1
                       
    j = 0
    bridge = [0] * n
    isPosible = True
    while j < n - 1:
        height = graph[j][i] - graph[j + 1][i]
        if height == 0:
            j += 1
            continue
        if abs(height) >= 2:
            isPosible = False
            break
        if bridge[j] != 0 and bridge[j] !=  height:
            isPosible = False
            break
        
        if height == 1: # 내려감
            for k in range(l):
                if j + k + 1 >= n:
                    isPosible = False
                    break
                if graph[j][i] - graph[j + 1 + k][i] != height:
                    isPosible = False
                    break
                bridge[j + k + 1] = 1
            j += l
                
        elif height == -1: # 올라감
            for k in range(l):
                if j - k < 0:
                    isPosible = False
                    break
                if graph[j - k][i] - graph[j + 1][i] != height:
                    isPosible = False
                    break
                if bridge[j - k] != 0:
                    isPosible = False
                    break
                bridge[j - k] = -1
            j += 1
        
        if isPosible == False:
            break
        
    if isPosible:
        cnt += 1
        
print(cnt)