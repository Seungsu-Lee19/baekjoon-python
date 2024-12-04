import sys
import copy
input = sys.stdin.readline

def change(_ch):
    if _ch == "B":
        return False
    elif _ch == "W":
        return True

N, M = list(map(int, input().split()))

board1 = []
for i in range(N):
    _str = input().rstrip()
    board1.append(list(map(change, _str)))

board2 = copy.deepcopy(board1)

cnt = 0
color1 = board1[0][0]
color2 = not board2[0][0]

change_board1 = [[0 for col in range(M)] for row in range(N)]
change_board2 = [[0 for col in range(M)] for row in range(N)]

for i in range(N):
    for j in range(M):
        if board1[i][j] == color1:
            change_board1[i][j] = 1
            board1[i][j] = not color1
        if board2[i][j] == color2:
            change_board2[i][j] = 1
            board2[i][j] = not color2
        
        color1 = board1[i][j]
        color2 = board2[i][j]

    color1 = board1[i][0]
    color2 = board2[i][0]

min_sum1 = float('inf') 
min_sum2 = float('inf')  
    
for i in range(N - 7):  
    for j in range(M - 7):  
        current_sum1 = 0
        current_sum2 = 0
        for x in range(8):
            for y in range(8):
                current_sum1 += change_board1[i + x][j + y]
                current_sum2 += change_board2[i + x][j + y]
        min_sum1 = min(min_sum1, current_sum1)
        min_sum2 = min(min_sum2, current_sum2)

print(min(min_sum1, min_sum2))
