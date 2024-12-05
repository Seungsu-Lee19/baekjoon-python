import sys
input = sys.stdin.readline

t = int(input())

prev_num = 1
cnt = 4

for i in range(t):
    cur_num = prev_num * 2
    
    for j in range(prev_num * 2 + 1):
        if j % 2 == 0:
            cnt += prev_num
        else:
            cnt += (prev_num * 2 + 1)

    prev_num = cur_num
print(cnt)
    
    