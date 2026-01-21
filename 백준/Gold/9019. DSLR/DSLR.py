from collections import deque

t = int(input())

a = 0
b = 0

def bfs():
    queue = deque()
    queue.append(a)
    
    visited = {}
    prev = {}
    how = {}
    
    visited[a] = []
    
    while queue:
        n = queue.popleft()
        
        if n == b:
            ret = []
            while n != a:
                ret.append(how[n])
                n = prev[n]
            
            for i in range(len(ret) - 1, -1, -1):
                print(ret[i], end="")
            print()
            return
        
        # D => n * 2 // 1000
        nextNum = (n * 2) % 10000
        if nextNum not in visited:
            visited[nextNum] = True
            prev[nextNum] = n
            how[nextNum] = 'D'
            queue.append(nextNum)

        # S
        nextNum = 9999 if n == 0 else n - 1
        if nextNum not in visited:
            visited[nextNum] = True
            prev[nextNum] = n
            how[nextNum] = 'S'
            queue.append(nextNum)
        
        # L
        nextNum = (n % 1000) * 10 + (n // 1000)
        if nextNum not in visited:
            visited[nextNum] = True
            prev[nextNum] = n
            how[nextNum] = 'L'
            queue.append(nextNum)
        
        # R
        nextNum = (n % 10) * 1000 + (n // 10)
        if nextNum not in visited:
            visited[nextNum] = True
            prev[nextNum] = n
            how[nextNum] = 'R'
            queue.append(nextNum)
        
    return -1


for _ in range(t):
    a, b = map(int, input().split())
    
    bfs()
    