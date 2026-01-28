n, k = map(int, input().split())
belt = list(map(int, input().split()))
robot = [False for _ in range(n)]

progress = 0
num = 0
while num < k:
    belt = [belt[-1]] + belt[:-1]
    robot = [False] + robot[:-1]
    robot[-1] = False
    
    for i in range(n - 2, -1, -1):
        if robot[i] == True and robot[i + 1] == False and belt[i + 1] > 0:
            robot[i] = False
            robot[i + 1] = True
            belt[i + 1] -= 1
            
            if belt[i + 1] == 0:
                num += 1
    
    if belt[0] > 0:
        belt[0] -= 1
        robot[0] = True
        if belt[0] == 0:
            num += 1
            
    progress += 1
    
print(progress)