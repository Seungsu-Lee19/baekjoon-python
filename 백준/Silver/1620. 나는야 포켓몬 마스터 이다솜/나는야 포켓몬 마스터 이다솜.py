N, M = map(int, input().split())

pocket_name = {}
pocket_num = {}
for i in range(1, N + 1):
    name = input()
    pocket_name[name] = i
    pocket_num[i] = name
    
for _ in range(M):
    cmd = input()
    if cmd in pocket_name:
        print(pocket_name[cmd])
    else:
        print(pocket_num[int(cmd)])