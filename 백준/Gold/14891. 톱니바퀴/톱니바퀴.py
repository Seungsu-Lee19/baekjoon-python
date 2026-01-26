wheel = [[]]
for _ in range(4):
    wheel.append(list(map(int, input().strip())))
    
k = int(input())
rot = []
for _ in range(k):
    rot.append(list(map(int, input().split())))
    
for i in range(k):
    idx = rot[i][0]
    direction = rot[i][1]
    candi = [(idx, direction)]
    
    if idx == 1:
        for j in range(2, 5):
            if wheel[idx][2] != wheel[j][6]:
                direction = -direction
                candi.append((j, direction))
                idx += 1
            else:
                break
    
    elif idx == 2:
        if wheel[1][2] != wheel[2][6]:
            candi.append((1, -direction))
        for j in range(3, 5):
            if wheel[idx][2] != wheel[j][6]:
                direction = -direction
                candi.append((j, direction))
                idx += 1
            else:
                break
    
    elif idx == 3:
        if wheel[3][2] != wheel[4][6]:
            candi.append((4, -direction))
        for j in range(2, 0, -1):
            if wheel[idx][6] != wheel[j][2]:
                direction = -direction
                candi.append((j, direction))
                idx -= 1
            else:
                break
    
    elif idx == 4:
        for j in range(3, 0, -1):
            if wheel[idx][6] != wheel[j][2]:
                direction = -direction
                candi.append((j, direction))
                idx -= 1
            else:
                break
    
    for idx, direction in candi:
        if direction == 1: # cw
            wheel[idx] = [wheel[idx][-1]] + wheel[idx][:-1]
        else:              # ccw
            wheel[idx] = wheel[idx][1:] + [wheel[idx][0]]

_sum = 0
for i in range(1, 5):
    if wheel[i][0] == 1:
        _sum = _sum + 2 ** (i - 1) 
print(_sum)