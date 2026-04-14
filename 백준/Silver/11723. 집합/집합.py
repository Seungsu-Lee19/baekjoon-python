import sys
input = sys.stdin.readline

M = int(input())

S = set()
for _ in range(M):
    cmd = list(input().split())
    
    if cmd[0] == 'add':
        x = int(cmd[1])
        S.add(x)
    elif cmd[0] == 'remove':
        x = int(cmd[1])
        S.discard(x)
    elif cmd[0] == 'check':
        x = int(cmd[1])
        print(1 if x in S else 0)
    elif cmd[0] == 'toggle':
        x = hash(int(cmd[1]))
        if x in S:
            S.discard(x)
        else:
            S.add(x)
    elif cmd[0] == 'all':
        for i in range(1, 21):
            S.add(i)
    elif cmd[0] == 'empty':
        S = set()
        