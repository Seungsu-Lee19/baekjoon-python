N = int(input())

graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))
    
white = 0
blue = 0
def sp(paper, n):
    global white, blue
    
    isSplit = False
    for i in range(n):
        for j in range(n):
            if paper[0][0] != paper[i][j]:
                isSplit = True
                break
        if isSplit:
            break
        
    if isSplit:
        new_n = n // 2
        
        if new_n == 1:
            for i in range(n):
                for j in range(n):
                    if paper[i][j] == 0:
                        white += 1
                    else:
                        blue += 1
            return
        
        new_paper1 = [[0 for _ in range(new_n)] for _ in range(new_n)]
        new_paper2 = [[0 for _ in range(new_n)] for _ in range(new_n)]
        new_paper3 = [[0 for _ in range(new_n)] for _ in range(new_n)]
        new_paper4 = [[0 for _ in range(new_n)] for _ in range(new_n)]
        for i in range(n):
            for j in range(n):
                if i < new_n and j < new_n: # 왼쪽 위
                    new_paper1[i][j] = paper[i][j]
                elif i < new_n and j >= new_n: # 오른쪽 위
                    new_paper2[i][j - new_n] = paper[i][j]
                elif i >= new_n and j < new_n: # 왼쪽 아래
                    new_paper3[i - new_n][j] = paper[i][j]
                elif i >= new_n and j >= new_n: # 오른쪽 아래
                    new_paper4[i - new_n][j - new_n] = paper[i][j]
                    
        sp(new_paper1, new_n)
        sp(new_paper2, new_n)
        sp(new_paper3, new_n)
        sp(new_paper4, new_n)
    
    else:
        if paper[0][0] == 0:
            white += 1
        else:
            blue += 1

sp(graph, N)
print(white)
print(blue)