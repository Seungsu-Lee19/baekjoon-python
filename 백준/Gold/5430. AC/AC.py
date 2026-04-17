from collections import deque
import sys
input = sys.stdin.readline

T = int(input())

ans = []

for _ in range(T):
    p = input()
    n = int(input())
    x = deque(eval(input()))
    
    a = None
    cur = False
    for cmd in p:
        if cmd == 'R':
            # x.reverse()
            cur = not cur
            
        elif cmd == 'D':
            if n == 0:
                a = 'error'
                break
            n -= 1
            
            if cur == False:
                x.popleft()
            else:
                x.pop()
            
    if a is None:
        if cur == True:
            x.reverse()
        ans.append('[' + ','.join(map(str, list(x))) + ']')
    else:
        ans.append(a)
        
for a in ans:
    print(a)
        