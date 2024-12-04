import sys
input = sys.stdin.readline

N, M = list(map(int, input().split()))

board = []
for i in range(N):
    board.append(input().rstrip())

cnt = []
for i in range(N - 7):
    for j in range(M - 7):
        w_cnt = 0
        b_cnt = 0

        for x in range(i, i + 8):
            for y in range(j, j + 8):
                if (x + y) % 2 == 0:
                    if board[x][y] == 'W':
                        b_cnt += 1
                    else:
                        w_cnt += 1 
                
                else:
                    if board[x][y] == 'W':
                        w_cnt += 1
                    else:
                        b_cnt += 1 
        cnt.append(w_cnt)
        cnt.append(b_cnt)

print(min(cnt))